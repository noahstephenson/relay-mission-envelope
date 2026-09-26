# Worked example: B2 at S2

Gross mass = 3.0 + 1.7 + 0.1 = 4.800 kg. Auxiliary bus demand = 32.000 W. Reference power is propulsion-only.

| Segment | Duration s | Bus W | Energy Wh |
|---|---:|---:|---:|
| climb | 33.333 | 1017.901 | 9.425 |
| outbound | 60.000 | 899.593 | 14.993 |
| establish | 30.000 | 820.720 | 6.839 |
| relay | 900.000 | 820.720 | 205.180 |
| return | 60.000 | 899.593 | 14.993 |
| descent | 50.000 | 702.412 | 9.756 |

Usable energy 324.000 Wh; reserve 64.800 Wh; planned allowance 259.200 Wh. Total mission 261.187 Wh gives signed margin -1.987 Wh.

Maximum energy-supported dwell = 891.286 s. Required dwell = 900.000 s. Failed assessed requirements: R2, R3.

All values are calculated from illustrative inputs. A passed numerical test is not hardware validation.
