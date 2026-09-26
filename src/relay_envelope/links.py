from math import pi,log10,dist
from .geometry import clearance

def hop(a,b,radio,wall):
    distance=dist(a,b)
    if distance <= 0: raise ValueError('Radio endpoints must be distinct')
    fspl=20*log10(4*pi*distance*radio['frequency_hz']/299792458)
    received=radio['tx_power_dbm']+radio['tx_gain_dbi']+radio['rx_gain_dbi']-radio['misc_loss_db']-fspl
    margin=received-radio['receiver_threshold_dbm']
    screen=clearance(a,b,wall)
    return dict(distance_m=distance,fspl_db=fspl,received_dbm=received,
                link_margin_db=margin,**screen,
                passes=screen['clear'] and margin>=radio['required_margin_db'])
