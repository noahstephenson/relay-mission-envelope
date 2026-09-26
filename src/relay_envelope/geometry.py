"""Straight paths through one idealized vertical screen."""
from math import dist

def clearance(a,b,wall):
    x=wall['x_m']; dx=b[0]-a[0]
    if dx == 0:
        if a[0] != x: return {"clear":True,"clearance_margin_m":None}
        z=min(a[2],b[2])
    else:
        t=(x-a[0])/dx
        if not 0 <= t <= 1: return {"clear":True,"clearance_margin_m":None}
        z=a[2]+t*(b[2]-a[2])
    margin=z-wall['top_z_m']-wall['clearance_m']
    return {"clear":margin>=0,"clearance_margin_m":margin}

def route_times(base,station,mission):
    height=station[2]-base[2]
    if height < 0: raise ValueError('Station below base is outside sequential route contract')
    horizontal=dist(base[:2],station[:2])
    return dict(climb=height/mission['climb_speed_mps'],
                outbound=horizontal/mission['transit_speed_mps'],
                establish=mission['establish_s'],relay=mission['dwell_s'],
                **{'return':horizontal/mission['transit_speed_mps']},
                descent=height/mission['descent_speed_mps'])
