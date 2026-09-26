import csv,json,hashlib,copy
from pathlib import Path
from .evaluate import evaluate,select,nondominated
from .links import hop

def run(config_path,output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    c=json.loads(Path(config_path).read_text(encoding='utf-8')); rows=evaluate(c)
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    canonical=json.dumps(c,sort_keys=True).encode(); sha=hashlib.sha256(canonical).hexdigest()
    (out/'resolved-inputs.json').write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8')
    result={'input_sha256':sha,'selection_status':'provisional; physics and hardware unreviewed','selected':select(rows),
            'nondominated':nondominated(rows),'direct_path':hop(*c['mission']['endpoints_m'],c['radio'],c['obstacle']),'options':rows}
    (out/'baseline.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    fields=['option_id','gross_mass_kg','usable_energy_wh','reserve_wh','mission_energy_wh','energy_margin_wh','max_energy_dwell_s','min_link_margin_db','assessed_gates_pass','model_domain_status']
    with (out/'comparison.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    md=['# Calculated baseline','',f"Provisional selection: **{result['selected']}**. All inputs are illustrative; physics and hardware remain unreviewed.",'', '| Option | Mass kg | Energy margin Wh | Max energy dwell min | Modeled gates |','|---|---:|---:|---:|---|']
    for r in rows:
        md.append(f"| {r['option_id']} | {r['gross_mass_kg']:.2f} | {r['energy_margin_wh']:.2f} | {r['max_energy_dwell_s']/60:.2f} | {', '.join(r['failed_requirements']) or 'pass'} |")
    md+=['', 'Energy dwell is not a service guarantee: clearance, link, mass and power gates also apply.', '',f'Input SHA-256: `{sha}`']
    (out/'summary.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    fig,ax=plt.subplots(figsize=(8,4));ax.bar([r['option_id'] for r in rows],[r['energy_margin_wh'] for r in rows]);ax.axhline(0,color='black',lw=.8);ax.set(ylabel='Energy margin (Wh)',title='Illustrative mission: energy after planned recovery and reserve');fig.tight_layout();fig.savefig(out/'energy-margin.png',dpi=160);plt.close(fig)
    sweeps=[]
    fig,ax=plt.subplots(figsize=(8,4))
    for i,r in enumerate(rows):
        ys=[]
        for dwell in c['experiment']['dwell_sweep_s']:
            case=copy.deepcopy(c);case['mission']['dwell_s']=dwell;res=evaluate(case);ys.append(res[i]['energy_margin_wh'])
            if i==0: sweeps.append({'dwell_s':dwell,'selected':select(res)})
        ax.plot([x/60 for x in c['experiment']['dwell_sweep_s']],ys,label=r['option_id'])
    ax.axhline(0,color='black',lw=.8);ax.set(xlabel='Requested service dwell (min)',ylabel='Energy margin (Wh)',title='Illustrative dwell sweep; other gates still apply');ax.legend(ncol=3);fig.tight_layout();fig.savefig(out/'dwell-sweep.png',dpi=160);plt.close(fig)
    sensitivity=[];fig,ax=plt.subplots(figsize=(8,4))
    for mult in c['physics']['sensitivity_power_multipliers']:
        res=evaluate(c,mult);sensitivity.append({'propulsion_multiplier':mult,'selected':select(res),'options':res})
    for i,r in enumerate(rows):ax.plot(c['physics']['sensitivity_power_multipliers'],[s['options'][i]['energy_margin_wh'] for s in sensitivity],marker='o',label=r['option_id'])
    ax.axhline(0,color='black',lw=.8);ax.set(xlabel='Shared propulsion power multiplier',ylabel='Energy margin (Wh)',title='Illustrative sensitivity, not a wind or probability model');ax.legend(ncol=3);fig.tight_layout();fig.savefig(out/'power-sensitivity.png',dpi=160);plt.close(fig)
    (out/'experiments.json').write_text(json.dumps({'dwell_sweep':sweeps,'power_sensitivity':sensitivity},indent=2)+'\n',encoding='utf-8')
    return result
