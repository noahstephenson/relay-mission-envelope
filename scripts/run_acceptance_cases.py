"""Small scenario checks; all mutations use copies of the frozen baseline."""
import json,copy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from relay_envelope.evaluate import evaluate,select

def run():
    baseline=json.loads((ROOT/'config/baseline.json').read_text(encoding='utf-8'));reports=[]
    def case(id,description,mutate,expected,multiplier=1):
        c=copy.deepcopy(baseline);mutate(c);rows=evaluate(c,multiplier);selected=select(rows)
        passed=selected==expected
        reports.append(dict(id=id,description=description,expected_selection=expected,actual_selection=selected,passed=passed,failed_gates={r['option_id']:r['failed_requirements'] for r in rows}))
    case('AC1','Frozen 900 s request; no model-feasible option',lambda c:None,'NO_FEASIBLE_OPTION')
    case('AC2','Separate 600 s mission request',lambda c:c['mission'].update(dwell_s=600),'B1-S2')
    case('AC3','Shared 10 percent lower propulsion demand',lambda c:None,'B2-S2',.9)
    case('AC4','Shared 10 percent higher propulsion demand',lambda c:None,'NO_FEASIBLE_OPTION',1.1)
    case('AC5','All masses exceed a deliberately reduced ceiling',lambda c:c['vehicle'].update(max_gross_mass_kg=3.9),'NO_FEASIBLE_OPTION')
    case('AC6','All bus demands exceed a deliberately reduced ceiling',lambda c:c['vehicle'].update(continuous_bus_limit_w=100),'NO_FEASIBLE_OPTION')
    case('AC7','Deliberately impossible radio threshold',lambda c:c['radio'].update(required_margin_db=100),'NO_FEASIBLE_OPTION')
    case('AC8','Mass range excludes both installed configurations',lambda c:c['physics'].update(mass_domain_kg=[3,3.5]),'NO_FEASIBLE_OPTION')
    out={'scope':'Model behavior on explicit scenario mutations, not physical validation','cases':reports,'passed':all(x['passed'] for x in reports)}
    (ROOT/'results/acceptance-cases.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(f"Acceptance cases: {sum(x['passed'] for x in reports)}/{len(reports)} passed")
    if not out['passed']:raise SystemExit(1)
if __name__=='__main__':run()
