# Numerical assumptions and open evidence

Which decisions are already made, and which numbers require evidence?

Every numerical value in `config/baseline.json` is an assistant-selected illustrative assumption. The common provenance record applies to every leaf, including experiment ranges. There are no measured or manufacturer-verified inputs. This choice makes the package executable without pretending a real aircraft has been selected.

| Group | Frozen choice | Why here | Owner / evidence needed |
|---|---|---|---|
| Aircraft | 3.0 kg nonbattery, 5.5 kg analysis ceiling, four 0.2 m radius rotors | Small fixed multirotor example | Noah: compatible hardware or keep conceptual |
| Packs | B1 1.0 kg / 220 Wh; B2 1.7 kg / 360 Wh + 0.1 kg mount | Different energy and installed mass | Noah: pack and mounting evidence |
| Supply | 22.2 V nominal, 1400 W continuous model ceiling | Common proposed interface | Noah: actual voltage range, discharge and connector limits |
| Propulsion | 600 W at 4 kg, exponent 1.5 | Provisional screening law | Michael: validity and discrepancy |
| Auxiliary | 12 W avionics; 18 W relay after 90% regulator | Explicit load accounting | Noah: radio and avionics evidence |
| Energy | 90% usable, 20% of usable withheld | Single unambiguous reserve basis | Joint: discharge basis and uncertainty |
| Route | 10 m/s horizontal, 3 m/s climb, 2 m/s descent | Sequential, inspectable timings | Michael: bound segment allowances |
| Links | 2.4 GHz, 20 dBm, 2 dBi each end, 2 dB losses, -90 dBm threshold, 10 dB margin | Uniform toy link screen | Noah: consistent modulation/rate basis and scheduling |
| Geometry | Thin wall; 5 m straight-ray clearance | Reject clearly blocked paths | Noah: preserve stated simplification |
| Domain | 3–5.5 kg assumed analysis range | Prevent silent extrapolation | Michael: supported range may be narrower |

No flight, throughput, obstruction diffraction, battery discharge or hardware-fit validation has occurred. The code checks internal consistency. Replace assumptions only with a recorded reason; preserve the original result when making a reviewed revision.

Aircraft and propulsion identifiers are conceptual. Rotor geometry documents the fixed-geometry assumption; it does not directly set the fitted reference power. No thrust feasibility claim is implemented until Michael supplies a justified model or limit.
