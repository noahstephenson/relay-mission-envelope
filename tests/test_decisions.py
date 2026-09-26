import unittest,json,copy,math
from pathlib import Path
from relay_envelope.evaluate import evaluate,select
from relay_envelope.boundaries import decision_boundaries

class DecisionTests(unittest.TestCase):
    def setUp(self):self.c=json.loads(Path('config/baseline.json').read_text())
    def test_energy_boundary_changes_decision(self):
        b=next(x for x in decision_boundaries(self.c) if x['option_id']=='B2-S2')
        alpha=b['energy_break_even_power_multiplier']
        self.assertTrue(evaluate(self.c,alpha-1e-6)[4]['checks']['R3'])
        self.assertFalse(evaluate(self.c,alpha+1e-6)[4]['checks']['R3'])
    def test_mass_and_power_gates_fail_independently(self):
        self.c['vehicle']['max_gross_mass_kg']=3.9
        self.assertTrue(all(not r['checks']['R4'] for r in evaluate(self.c)))
        self.c['vehicle']['max_gross_mass_kg']=5.5;self.c['vehicle']['continuous_bus_limit_w']=100
        self.assertTrue(all(not r['checks']['R5'] for r in evaluate(self.c)))
    def test_tie_break_order(self):
        def row(id,m,e,l):return dict(option_id=id,gross_mass_kg=m,energy_margin_wh=e,min_link_margin_db=l,eligible_for_provisional_selection=True)
        self.assertEqual(select([row('b',4,1,20),row('a',5,100,40)]),'b')
        self.assertEqual(select([row('b',4,1,20),row('a',4,2,10)]),'a')
        self.assertEqual(select([row('b',4,2,20),row('a',4,2,10)]),'b')
        self.assertEqual(select([row('b',4,2,20),row('a',4,2,20)]),'a')
    def test_nonpositive_multiplier_rejected(self):
        for value in [0,-1,float('nan'),float('inf')]:
            with self.assertRaises(ValueError):evaluate(self.c,value)
    def test_relaxed_dwell_retains_same_architecture(self):
        self.c['mission']['dwell_s']=600
        rows=evaluate(self.c)
        self.assertEqual(select(rows),'B1-S2')
        self.assertFalse(rows[0]['checks']['R1'])

if __name__=='__main__':unittest.main()
