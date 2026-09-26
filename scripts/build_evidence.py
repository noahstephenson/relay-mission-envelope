"""Generate decision explanation, worked ledger and illustrative boundary figure."""
import json,copy,hashlib,sys,platform
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from relay_envelope.evaluate import evaluate,select
from relay_envelope.boundaries import decision_boundaries

def build():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    c=json.loads((ROOT/'config/baseline.json').read_text(encoding='utf-8'));rows=evaluate(c);out=ROOT/'results'
    bounds=decision_boundaries(c)
    (out/'decision-boundaries.json').write_text(json.dumps({'status':'analytic boundaries of the illustrative model; not supported physical uncertainty bounds','options':bounds},indent=2)+'\n',encoding='utf-8')
    text=['# Decision brief','',f"At a requested dwell of {c['mission']['dwell_s']/60:.3f} minutes, the provisional selector returns **{select(rows)}**. This is an energy-and-geometry screen under illustrative assumptions, not a physical infeasibility proof.",'', '| Option | What limits it at baseline? | Energy break-even multiplier |','|---|---|---:|']
    for row,b in zip(rows,bounds):
        reasons=[]
        if not row['checks']['R1']:reasons.append('Service hop clearance or link fails')
        if not row['checks']['R3']:reasons.append(f"Energy shortfall {-row['energy_margin_wh']:.2f} Wh")
        if not row['checks']['R4']:reasons.append('Gross mass exceeds ceiling')
        if not row['checks']['R5']:reasons.append('Continuous demand exceeds ceiling')
        text.append(f"| {row['option_id']} | {'; '.join(reasons) or 'Passes modeled gates'} | {b['energy_break_even_power_multiplier']:.4f} |")
    target=next(x for x in rows if x['option_id']=='B2-S2');boundary=next(x for x in bounds if x['option_id']=='B2-S2')
    text+=['', '## What the near-boundary result means','',f"B2-S2 supports {target['max_energy_dwell_s']/60:.3f} minutes in the current model. At the requested dwell its energy boundary occurs at propulsion multiplier {boundary['energy_break_even_power_multiplier']:.5f}. A small change in the assumed power can therefore change the screening decision. This is a reason to ask Michael for a defensible error bound, not a reason to round the option into feasibility.",'', 'B2-S1 has more energy margin but a blocked far hop. More pack energy does not repair that geometric failure. A lower dwell request is a different mission and must be labeled as a separate case.', '', '## Local sensitivity meaning','', 'For fixed installed mass and times, E(alpha)=alpha E_propulsion + E_auxiliary, so the energy break-even multiplier is (planned allowance − E_auxiliary)/E_propulsion. A separate continuous-power cap must also hold. Mass and radio gates do not change in this one-parameter experiment. The provided sweep is illustrative, not an empirically established uncertainty interval.']
    (out/'decision-brief.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    # Station-specific energy boundary, all curves retain failed geometry options.
    fig,ax=plt.subplots(figsize=(8,4.5));alphas=[.8+i*.005 for i in range(81)]
    for i,row in enumerate(rows):
        ys=[evaluate(c,a)[i]['max_energy_dwell_s']/60 for a in alphas]
        style='--' if not row['checks']['R1'] else '-'
        ax.plot(alphas,ys,style,label=row['option_id']+(' (link screen fails)' if not row['checks']['R1'] else ''))
    ax.axhline(c['mission']['dwell_s']/60,color='black',lw=1,label='Requested dwell')
    ax.axvline(1,color='gray',lw=.8);ax.set(xlabel='Shared propulsion power multiplier',ylabel='Maximum energy-supported dwell (min)',title='Illustrative model boundary: fixed geometry and reserve')
    ax.legend(ncol=2,fontsize=8);fig.tight_layout();fig.savefig(out/'decision-boundary.png',dpi=160);plt.close(fig)
    # Regenerate worked case rather than letting its prose diverge from numbers.
    b=next(b for b in c['batteries'] if b['id']=='B2');v=c['vehicle'];mission=c['mission']
    aux=v['avionics_power_w']+v['payload_load_w']/v['regulator_efficiency']
    worked=['# Worked example: B2 at S2','',f"Gross mass = {v['nonbattery_mass_kg']} + {b['battery_mass_kg']} + {b['mount_delta_kg']} = {target['gross_mass_kg']:.3f} kg. Auxiliary bus demand = {aux:.3f} W. Reference power is propulsion-only.",'', '| Segment | Duration s | Bus W | Energy Wh |','|---|---:|---:|---:|']
    for seg in target['ledger']:worked.append(f"| {seg['segment']} | {seg['duration_s']:.3f} | {seg['bus_power_w']:.3f} | {seg['energy_wh']:.3f} |")
    worked+=['',f"Usable energy {target['usable_energy_wh']:.3f} Wh; reserve {target['reserve_wh']:.3f} Wh; planned allowance {target['planned_allowance_wh']:.3f} Wh. Total mission {target['mission_energy_wh']:.3f} Wh gives signed margin {target['energy_margin_wh']:.3f} Wh.",'',f"Maximum energy-supported dwell = {target['max_energy_dwell_s']:.3f} s. Required dwell = {mission['dwell_s']:.3f} s. Failed assessed requirements: {', '.join(target['failed_requirements']) or 'none'}.",'','All values are calculated from illustrative inputs. A passed numerical test is not hardware validation.']
    (out/'worked-example.md').write_text('\n'.join(worked)+'\n',encoding='utf-8')
    files=sorted([*ROOT.glob('src/**/*.py'),*ROOT.glob('scripts/*.py'),*ROOT.glob('physics/*.py'),*ROOT.glob('tests/*.py'),ROOT/'config/baseline.json',ROOT/'model/architecture.json'])
    manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (out/'source-provenance.json').write_text(json.dumps({'python':platform.python_version(),'matplotlib':matplotlib.__version__,'git_commit':None,'note':'No repository commit yet; source bytes identified individually','files_sha256':manifest},indent=2)+'\n',encoding='utf-8')
    print('Built decision boundaries, brief, worked case and source provenance')
if __name__=='__main__':build()
