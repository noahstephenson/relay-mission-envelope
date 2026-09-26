"""Stable option evaluator and deterministic selector."""
import math
from .energy import energy
from .links import hop

def validate(c):
    def walk(x):
        if isinstance(x,dict):
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
        elif isinstance(x,(int,float)) and not math.isfinite(x): raise ValueError('Nonfinite input')
    walk(c)
    v=c['vehicle']; m=c['mission']; p=c['physics']
    if not math.isclose(sum(v['mass_components_kg'].values()),v['nonbattery_mass_kg']): raise ValueError('Mass breakdown mismatch')
    for k in ('transit_speed_mps','climb_speed_mps','descent_speed_mps'):
        if m[k]<=0: raise ValueError(k)
    for k in ('dwell_s','establish_s'):
        if m[k]<0: raise ValueError(k)
    if not 0<m['usable_fraction']<=1 or not 0<=m['reserve_fraction']<1: raise ValueError('Energy fractions')
    if not 0<v['regulator_efficiency']<=1: raise ValueError('Regulator efficiency')
    for k in ('nonbattery_mass_kg','max_gross_mass_kg','continuous_bus_limit_w'):
        if v[k]<=0: raise ValueError(k)
    if any(x<0 for x in v['mass_components_kg'].values()): raise ValueError('Negative mass')
    if min(v['avionics_power_w'],v['payload_load_w'])<0: raise ValueError('Negative load')
    if min(p['reference_power_w'],p['reference_mass_kg'],*p['segment_factors'].values(),*p['sensitivity_power_multipliers'])<=0: raise ValueError('Power model')
    if not 0<p['mass_domain_kg'][0]<=p['mass_domain_kg'][1]: raise ValueError('Mass domain')
    if len(c['batteries'])!=2 or len(c['stations'])!=3: raise ValueError('Expected two batteries and three stations')
    for group in ('batteries','stations'):
        if len({x['id'] for x in c[group]})!=len(c[group]): raise ValueError('Duplicate ID')
    for b in c['batteries']:
        if min(b['battery_mass_kg'],b['nominal_energy_wh'])<=0 or b['mount_delta_kg']<0: raise ValueError('Battery values')
        if b['voltage_v']!=v['bus_voltage_v']: raise ValueError('Incompatible assumed voltage')
    if c['radio']['frequency_hz']<=0: raise ValueError('Frequency')
    if c['radio']['required_margin_db']<0 or c['radio']['misc_loss_db']<0: raise ValueError('Radio margin/loss')
    if c['obstacle']['clearance_m']<0: raise ValueError('Negative geometric clearance')
    if v['bus_voltage_v']<=0 or v['rotor_radius_m']<=0 or v['rotor_count']<1 or int(v['rotor_count'])!=v['rotor_count']: raise ValueError('Vehicle geometry/voltage')
    if set(p['segment_factors'])!={'climb','outbound','establish','relay','return','descent'}: raise ValueError('Segment factor names')
    if any(t<0 for t in c['experiment']['dwell_sweep_s']): raise ValueError('Negative dwell sweep')
    for point in [m['base_m'],*m['endpoints_m'],*[s['position_m'] for s in c['stations']]]:
        if len(point)!=3: raise ValueError('ENU position requires three coordinates')
    if len(m['endpoints_m'])!=2: raise ValueError('Two endpoints required')
    if any(s['position_m'][2]<m['base_m'][2] for s in c['stations']): raise ValueError('Station below base')
    if m['endpoints_m'][0]==m['endpoints_m'][1] or any(s['position_m'] in m['endpoints_m'] for s in c['stations']): raise ValueError('Coincident radio endpoints')

def evaluate_option(vehicle,battery,station,mission,physics,radio,obstacle,power_multiplier=1):
    if not math.isfinite(power_multiplier) or power_multiplier<=0: raise ValueError('Power multiplier must be finite and positive')
    e=energy(vehicle,battery,station,mission,physics,power_multiplier)
    a,b=mission['endpoints_m']; s=station['position_m']
    hops=[hop(a,s,radio,obstacle),hop(s,b,radio,obstacle)]
    checks={'R1':all(h['passes'] for h in hops),'R2':e['max_energy_dwell_s']>=mission['dwell_s']-1e-9,
            'R3':e['energy_margin_wh']>=-1e-9,'R4':e['gross_mass_kg']<=vehicle['max_gross_mass_kg'],
            'R5':e['max_bus_power_w']<=vehicle['continuous_bus_limit_w']}
    in_domain=physics['mass_domain_kg'][0]<=e['gross_mass_kg']<=physics['mass_domain_kg'][1]
    return dict(option_id=battery['id']+'-'+station['id'],battery_mass_kg=battery['battery_mass_kg'],mount_delta_kg=battery['mount_delta_kg'],**e,hops=hops,checks=checks,
                min_link_margin_db=min(h['link_margin_db'] for h in hops),
                mass_margin_kg=vehicle['max_gross_mass_kg']-e['gross_mass_kg'],
                power_margin_w=vehicle['continuous_bus_limit_w']-e['max_bus_power_w'],
                assessed_gates_pass=all(checks.values()),failed_requirements=[k for k,v in checks.items() if not v],
                unassessed_requirements=['R6 hardware compatibility'],physics_review_status='pending Michael',
                model_domain_status='within assumed range' if in_domain else 'outside assumed range',
                eligible_for_provisional_selection=all(checks.values()) and in_domain)

def evaluate(c,power_multiplier=1):
    validate(c)
    return [evaluate_option(c['vehicle'],b,s,c['mission'],c['physics'],c['radio'],c['obstacle'],power_multiplier)
            for b in c['batteries'] for s in c['stations']]

def select(rows):
    eligible=[r for r in rows if r['eligible_for_provisional_selection']]
    if not eligible: return 'NO_FEASIBLE_OPTION'
    return min(eligible,key=lambda r:(r['gross_mass_kg'],-r['energy_margin_wh'],-r['min_link_margin_db'],r['option_id']))['option_id']

def nondominated(rows):
    valid=[r for r in rows if r['eligible_for_provisional_selection']]
    return [r['option_id'] for r in valid if not any(
        q['gross_mass_kg']<=r['gross_mass_kg'] and q['max_energy_dwell_s']>=r['max_energy_dwell_s'] and
        (q['gross_mass_kg']<r['gross_mass_kg'] or q['max_energy_dwell_s']>r['max_energy_dwell_s']) for q in valid)]
