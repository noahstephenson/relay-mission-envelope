"""Assistant-prepared algebra checks. Michael has not reviewed this model.
No data fitting, validated uncertainty bounds, or research conclusion is implied.
"""
import json
from pathlib import Path
from relay_envelope.geometry import route_times
from relay_envelope.evaluate import evaluate

def dwell(mu,H,tau,lam,tq):
    f=(1+mu)**1.5
    return (H*mu-f*tau-lam*tq)/(f+lam)

def derivative(mu,H,tau,lam,tq):
    f=(1+mu)**1.5; fp=1.5*(1+mu)**.5
    n=H*mu-f*tau-lam*tq; d=f+lam
    return ((H-fp*tau)*d-n*fp)/d**2

def packet(c,b,s):
    # Treat option-specific mount increment as nonbattery mass; don't bury it in pack energy density.
    md=c['vehicle']['nonbattery_mass_kg']+b['mount_delta_kg'];mb=b['battery_mass_kg']
    p=c['physics'];v=c['vehicle'];m=c['mission']
    p0=p['reference_power_w']*(md/p['reference_mass_kg'])**1.5
    aux=v['avionics_power_w']+v['payload_load_w']/v['regulator_efficiency']
    times=route_times(m['base_m'],s['position_m'],m)
    tq=sum(t for name,t in times.items() if name!='relay')
    tau=sum(t*p['segment_factors'][name] for name,t in times.items() if name!='relay')
    eb=b['nominal_energy_wh']*3600/mb
    return dict(mu=mb/md,H=m['usable_fraction']*(1-m['reserve_fraction'])*eb*md/p0,
                tau=tau,lam=aux/p0,tq=tq)

def check():
    c=json.loads(Path('config/baseline.json').read_text())
    if c['physics']['segment_factors']['relay']!=1: raise ValueError('Starter assumes relay multiplier=1')
    rows=evaluate(c);results=[]
    for b in c['batteries']:
        for s in c['stations']:
            p=packet(c,b,s);t=dwell(**p);d=derivative(**p);h=1e-5
            left=dict(p,mu=p['mu']-h);right=dict(p,mu=p['mu']+h)
            fd=(dwell(**right)-dwell(**left))/(2*h)
            row=next(r for r in rows if r['option_id']==b['id']+'-'+s['id'])
            assert abs(t-row['max_energy_dwell_s'])<1e-8
            assert abs(d-fd)<1e-5
            results.append(dict(option_id=row['option_id'],**p,dwell_s=t,derivative_s=d,finite_difference_s=fd))
    assert abs(derivative(2,1,0,0,0))<1e-12
    print(json.dumps({'status':'assistant-prepared algebra checks only; Michael review pending','cases':results},indent=2))
if __name__=='__main__':check()
