"""Compare declared mission demands with the calculated screening capability."""
import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def build():
    c=json.loads((ROOT/'config/baseline.json').read_text(encoding='utf-8'));b=json.loads((ROOT/'results/baseline.json').read_text(encoding='utf-8'))
    assert b['input_sha256']==hashlib.sha256(json.dumps(c,sort_keys=True).encode()).hexdigest(),'Stale baseline'
    rows=[]
    for x in b['options']:
        clearances=[h['clearance_margin_m'] for h in x['hops'] if h['clearance_margin_m'] is not None]
        rows.append(dict(option_id=x['option_id'],required_dwell_s=c['mission']['dwell_s'],calculated_energy_dwell_s=x['max_energy_dwell_s'],dwell_surplus_s=x['max_energy_dwell_s']-c['mission']['dwell_s'],energy_surplus_wh=x['energy_margin_wh'],link_surplus_db=x['min_link_margin_db']-c['radio']['required_margin_db'],clearance_surplus_m=min(clearances) if clearances else None,mass_surplus_kg=x['mass_margin_kg'],power_surplus_w=x['power_margin_w'],assessed_gates_pass=x['assessed_gates_pass'],failed_requirements=x['failed_requirements'],evidence_status='conditional on illustrative inputs; hardware and physical validation pending'))
    report={'input_sha256':b['input_sha256'],'interpretation':'Positive surplus meets the corresponding numeric screen; zero meets equality; negative is a shortfall. Missing obstacle intersection is not a measured clearance. Dwell is an energy proxy, not demonstrated service.','options':rows}
    (ROOT/'results/mission-gap.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'results/mission-gap.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows([{**x,'failed_requirements':';'.join(x['failed_requirements'])} for x in rows])
    md=['# Mission demand versus calculated capability','','The mission demand is held fixed while each candidate capability is calculated from the same model. These are conditional engineering screens, not validated aircraft performance.','', f"Required relay dwell: **{c['mission']['dwell_s']:.0f} s**. Reserve: **{100*c['mission']['reserve_fraction']:.0f}% of usable energy**. Required hop margin: **{c['radio']['required_margin_db']:.0f} dB**.",'', '| Option | Energy-supported dwell s | Dwell surplus s | Energy surplus Wh | Link surplus dB | Clearance surplus m | Failed gates |','|---|---:|---:|---:|---:|---:|---|']
    for x in rows:
        clear='No intersection' if x['clearance_surplus_m'] is None else f"{x['clearance_surplus_m']:.2f}"
        md.append(f"| {x['option_id']} | {x['calculated_energy_dwell_s']:.2f} | {x['dwell_surplus_s']:.2f} | {x['energy_surplus_wh']:.2f} | {x['link_surplus_db']:.2f} | {clear} | {', '.join(x['failed_requirements']) or 'none'} |")
    md+=['', 'Dwell and energy shortfall are related expressions of the same resource constraint; they are not two independent pieces of physical evidence. Link surplus alone does not override blocked geometry. Detailed mass and power surpluses are retained in the JSON/CSV.','', '## What remains unresolved','', '- R6: interface definitions exist; Noah has not accepted installation compatibility and hardware evidence is absent.','- R7/R8: generated artifacts can be inspected and reproduced; this does not validate the aircraft.','- Michael must establish the supported physical domain and justified discrepancy bounds before this screening result supports a physical recommendation.','', '## Response to a gap','', 'Retain the failed option and state the limiting condition. Seek evidence for uncertain inputs or explicitly change the mission as a new labeled case. Do not silently relax thresholds, round away a shortfall, or tune inputs to produce a preferred winner.']
    (ROOT/'results/mission-gap.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print('Generated six-option mission demand/capability gap review')
if __name__=='__main__':build()
