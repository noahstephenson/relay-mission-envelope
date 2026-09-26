import unittest,json,copy,math
from pathlib import Path
from relay_envelope.energy import energy
from relay_envelope.geometry import clearance,route_times
from relay_envelope.links import hop
from relay_envelope.evaluate import evaluate,select,validate

class ModelTests(unittest.TestCase):
    def setUp(self): self.c=json.loads(Path('config/baseline.json').read_text())
    def test_independent_energy_ledger(self):
        r=evaluate(self.c)[0]
        # B1 mass=4 kg; propulsion=600 W; auxiliaries=12+18/.9=32 W.
        times=[50/3,25,30,900,25,25]; powers=[782,692,632,632,692,542]
        expected=sum(t*p/3600 for t,p in zip(times,powers))
        self.assertAlmostEqual(r['mission_energy_wh'],expected)
        self.assertAlmostEqual(r['energy_margin_wh'],220*.9*.8-expected)
        self.assertAlmostEqual(r['reserve_wh'],39.6)
    def test_reserve_equality_and_shortfall(self):
        c=self.c;r=evaluate(c)[1];c['mission']['dwell_s']=r['max_energy_dwell_s']
        self.assertTrue(evaluate(c)[1]['checks']['R3'])
        c['mission']['dwell_s']+=1
        self.assertFalse(evaluate(c)[1]['checks']['R3'])
    def test_clearance_cases(self):
        w=self.c['obstacle']
        self.assertFalse(clearance([0,0,2],[1200,0,2],w)['clear'])
        self.assertTrue(clearance([0,0,100],[1200,0,100],w)['clear'])
        self.assertTrue(clearance([0,0,40],[1200,0,40],w)['clear'])
        self.assertFalse(clearance([600,0,2],[600,10,100],w)['clear'])
    def test_link_arithmetic(self):
        r=hop([0,0,100],[1000,0,100],self.c['radio'],self.c['obstacle'])
        self.assertAlmostEqual(r['fspl_db'],100.052008056,places=6)
        self.assertAlmostEqual(r['link_margin_db'],11.947991944,places=6)
    def test_mass_power_and_return(self):
        rows=evaluate(self.c)
        self.assertAlmostEqual(rows[3]['gross_mass_kg'],4.8)
        self.assertGreater(rows[3]['max_bus_power_w'],rows[0]['max_bus_power_w'])
        self.assertEqual([x['segment'] for x in rows[0]['ledger']],['climb','outbound','establish','relay','return','descent'])
    def test_no_feasible_and_negative_dwell(self):
        for b in self.c['batteries']: b['nominal_energy_wh']=1
        rows=evaluate(self.c)
        self.assertEqual(select(rows),'NO_FEASIBLE_OPTION')
        self.assertTrue(all(r['max_energy_dwell_s']<0 for r in rows))
    def test_deterministic_and_outside_domain(self):
        rows=evaluate(self.c);self.assertEqual(len(rows),6)
        self.assertEqual(rows,evaluate(self.c));self.assertEqual(select(rows),select(list(reversed(rows))))
        self.c['physics']['mass_domain_kg']=[3,3.5]
        self.assertEqual(select(evaluate(self.c)),'NO_FEASIBLE_OPTION')
    def test_invalid_input(self):
        for key,value in [('transit_speed_mps',0),('reserve_fraction',1),('dwell_s',-1)]:
            c=copy.deepcopy(self.c);c['mission'][key]=value
            with self.assertRaises(ValueError):validate(c)
        c=copy.deepcopy(self.c);c['vehicle']['nonbattery_mass_kg']=float('nan')
        with self.assertRaises(ValueError):validate(c)
    def test_shared_power_increase_reduces_margin(self):
        a=evaluate(self.c,.9);b=evaluate(self.c,1.1)
        self.assertTrue(all(x['energy_margin_wh']>y['energy_margin_wh'] for x,y in zip(a,b)))

if __name__=='__main__':unittest.main()
