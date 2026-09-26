from .geometry import route_times

def energy(vehicle,battery,station,mission,physics,power_multiplier=1.0):
    mass=vehicle['nonbattery_mass_kg']+battery['battery_mass_kg']+battery['mount_delta_kg']
    hover=physics['reference_power_w']*(mass/physics['reference_mass_kg'])**1.5*power_multiplier
    aux=vehicle['avionics_power_w']+vehicle['payload_load_w']/vehicle['regulator_efficiency']
    times=route_times(mission['base_m'],station['position_m'],mission)
    ledger=[]
    for segment,seconds in times.items():
        power=hover*physics['segment_factors'][segment]+aux
        ledger.append(dict(segment=segment,duration_s=seconds,bus_power_w=power,energy_wh=power*seconds/3600))
    usable=battery['nominal_energy_wh']*mission['usable_fraction']
    reserve=usable*mission['reserve_fraction']; allowance=usable-reserve
    total=sum(x['energy_wh'] for x in ledger)
    nonservice=sum(x['energy_wh'] for x in ledger if x['segment']!='relay')
    service_power=hover*physics['segment_factors']['relay']+aux
    return dict(gross_mass_kg=mass,usable_energy_wh=usable,reserve_wh=reserve,
                planned_allowance_wh=allowance,mission_energy_wh=total,
                nonservice_energy_wh=nonservice,energy_margin_wh=allowance-total,
                service_energy_available_wh=allowance-nonservice,
                max_energy_dwell_s=(allowance-nonservice)*3600/service_power,
                max_bus_power_w=max(x['bus_power_w'] for x in ledger),ledger=ledger)
