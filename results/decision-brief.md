# Decision brief

At a requested dwell of 15.000 minutes, the provisional selector returns **NO_FEASIBLE_OPTION**. This is an energy-and-geometry screen under illustrative assumptions, not a physical infeasibility proof.

| Option | What limits it at baseline? | Energy break-even multiplier |
|---|---|---:|
| B1-S1 | Service hop clearance or link fails; Energy shortfall 21.86 Wh | 0.8723 |
| B1-S2 | Energy shortfall 42.70 Wh | 0.7765 |
| B1-S3 | Energy shortfall 53.93 Wh | 0.7326 |
| B2-S1 | Service hop clearance or link fails | 1.1115 |
| B2-S2 | Energy shortfall 1.99 Wh | 0.9921 |
| B2-S3 | Energy shortfall 16.57 Wh | 0.9375 |

## What the near-boundary result means

B2-S2 supports 14.855 minutes in the current model. At the requested dwell its energy boundary occurs at propulsion multiplier 0.99209. A small change in the assumed power can therefore change the screening decision. This is a reason to ask Michael for a defensible error bound, not a reason to round the option into feasibility.

B2-S1 has more energy margin but a blocked far hop. More pack energy does not repair that geometric failure. A lower dwell request is a different mission and must be labeled as a separate case.

## Local sensitivity meaning

For fixed installed mass and times, E(alpha)=alpha E_propulsion + E_auxiliary, so the energy break-even multiplier is (planned allowance − E_auxiliary)/E_propulsion. A separate continuous-power cap must also hold. Mass and radio gates do not change in this one-parameter experiment. The provided sweep is illustrative, not an empirically established uncertainty interval.
