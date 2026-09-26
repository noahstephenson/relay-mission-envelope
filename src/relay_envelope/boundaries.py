"""Algebraic screening boundaries; no inferred uncertainty distribution."""
from .evaluate import evaluate

def decision_boundaries(config):
    rows=evaluate(config)
    aux=config['vehicle']['avionics_power_w']+config['vehicle']['payload_load_w']/config['vehicle']['regulator_efficiency']
    records=[]
    for row in rows:
        auxiliary_wh=sum(s['duration_s']*aux/3600 for s in row['ledger'])
        propulsion_wh=row['mission_energy_wh']-auxiliary_wh
        peak_propulsion=max(s['bus_power_w']-aux for s in row['ledger'])
        # For fixed configuration and route: E(alpha)=alpha*E_propulsion+E_auxiliary.
        alpha_energy=(row['planned_allowance_wh']-auxiliary_wh)/propulsion_wh
        alpha_power=(config['vehicle']['continuous_bus_limit_w']-aux)/peak_propulsion
        cap=min(alpha_energy,alpha_power)
        fixed_gates_pass=row['checks']['R1'] and row['checks']['R4'] and row['model_domain_status']=='within assumed range'
        records.append(dict(option_id=row['option_id'],energy_break_even_power_multiplier=alpha_energy,
                            power_ceiling_multiplier=alpha_power,maximum_admissible_power_multiplier=cap,
                            fixed_gates_pass=fixed_gates_pass,requested_dwell_s=config['mission']['dwell_s'],
                            max_energy_dwell_s=row['max_energy_dwell_s'],
                            interpretation='Passes modeled gates for 0 < multiplier <= cap under fixed assumptions' if fixed_gates_pass and cap>0 else 'Fixed gate or nonpositive allowance prevents this boundary from admitting the option'))
    return records
