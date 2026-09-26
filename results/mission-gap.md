# Mission demand versus calculated capability

The mission demand is held fixed while each candidate capability is calculated from the same model. These are conditional engineering screens, not validated aircraft performance.

Required relay dwell: **900 s**. Reserve: **20% of usable energy**. Required hop margin: **10 dB**.

| Option | Energy-supported dwell s | Dwell surplus s | Energy surplus Wh | Link surplus dB | Clearance surplus m | Failed gates |
|---|---:|---:|---:|---:|---:|---|
| B1-S1 | 775.47 | -124.53 | -21.86 | 2.38 | -7.68 | R1, R2, R3 |
| B1-S2 | 656.76 | -243.24 | -42.70 | 6.27 | 60.00 | R2, R3 |
| B1-S3 | 592.80 | -307.20 | -53.93 | 4.86 | 88.86 | R2, R3 |
| B2-S1 | 1010.08 | 110.08 | 25.10 | 2.38 | -7.68 | R1 |
| B2-S2 | 891.29 | -8.71 | -1.99 | 6.27 | 60.00 | R2, R3 |
| B2-S3 | 827.30 | -72.70 | -16.57 | 4.86 | 88.86 | R2, R3 |

Dwell and energy shortfall are related expressions of the same resource constraint; they are not two independent pieces of physical evidence. Link surplus alone does not override blocked geometry. Detailed mass and power surpluses are retained in the JSON/CSV.

## What remains unresolved

- R6: interface definitions exist; Noah has not accepted installation compatibility and hardware evidence is absent.
- R7/R8: generated artifacts can be inspected and reproduced; this does not validate the aircraft.
- Michael must establish the supported physical domain and justified discrepancy bounds before this screening result supports a physical recommendation.

## Response to a gap

Retain the failed option and state the limiting condition. Seek evidence for uncertain inputs or explicitly change the mission as a new labeled case. Do not silently relax thresholds, round away a shortfall, or tune inputs to produce a preferred winner.
