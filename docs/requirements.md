# Requirements and evidence

What must each option meet, and what can this model actually verify?

These are analyst-defined requirements for a conceptual study. Numeric screens use assumed thresholds; hardware and real service performance remain unassessed. Model definitions are in `model/architecture.json`.

| ID | Requirement | Evidence status |
|---|---|---|
| R1 | For each declared service hop, the analysis shall require clearance margin at least 0 m relative to the wall top plus 5 m and link margin at least 10 dB above the -90 dBm assumed receiver threshold. | conditional calculation |
| R2 | Under the declared continuous-service assumptions, the analysis shall require energy-supported relay dwell of at least mission.dwell_s (baseline 900 s). | energy proxy; actual service unassessed |
| R3 | For each option, planned mission energy plus reserve shall not exceed nominal_energy_wh times usable_fraction. Reserve is reserve_fraction of usable energy. | conditional calculation |
| R4 | For each option, installed gross mass shall not exceed vehicle.max_gross_mass_kg (baseline 5.5 kg). | assumed ceiling |
| R5 | For each option, the highest modeled segment bus demand shall not exceed vehicle.continuous_bus_limit_w (baseline 1400 W). Transients remain unassessed. | assumed ceiling |
| R6 | The architecture shall specify I1–I5, their load and connection assumptions, and evidence gaps before a configuration is accepted for physical implementation. | architecture accepted; hardware unassessed |
| R7 | The study shall report pack and gross mass, usable and reserve energy, energy margin and maximum supported dwell for each of the six options. | artifact inspection |
| R8 | Each generated study shall preserve resolved inputs and their SHA-256, state provisional physics and evidence status, and identify the calculation source. | artifact inspection |

## Implemented trace
| Need | Requirement | Function | Logical | Physical | Interface | Evidence now |
|---|---|---|---|---|---|---|
| N1 | R1 | F3 | L3 | P5 | I4 | Straight-wall and free-space arithmetic tests; service scheduling assumed |
| N1 | R2 | F3,F6 | L3,L4 | P1,P2,P5 | I1,I2,I4 | Calculated energy dwell; actual service unassessed |
| N2 | R3 | F4,F5,F6 | L1,L2,L4 | P1–P4 | I1 | Ledger, reserve equality and shortfall tests |
| N2 | R4 | F2 | L2 | P6 | I3 | Mass arithmetic against assumed 5.5 kg ceiling |
| N2 | R5 | F6 | L4 | P1,P2,P4 | I1 | Maximum segment bus power against assumed 1400 W |
| N2,N3 | R6 | F1 | L1,L4 | P1,P2,P5,P6 | I1–I5 | Specified conceptually; hardware compatibility unassessed |
| N3 | R7 | F1 | L1 | Operator support | Not applicable | Generated CSV/JSON |
| N4 | R8 | F1,F4 | L1 | Operator support | Not applicable | Resolved input snapshot and SHA-256 |

Numerical R1–R5 pass/fail is conditional on assumed inputs. R6 is never promoted to a hardware pass. R7/R8 describe artifact completeness rather than flight performance. `NO_FEASIBLE_OPTION` means none passes the provisional calculation, not proof no real design can work.

## Verification responsibility and closure criteria

| Requirement | Verification method | Owner | Current evidence | Still needed |
|---|---|---|---|---|
| R1 | Geometry and link-budget analysis; independent fixtures | Noah | Known clear/blocked paths and 1 km RF calculation; per-hop outputs | Evidence for radio/service assumptions; actual throughput remains unassessed |
| R2 | Compare energy-supported dwell to requested dwell | Noah calculation; Michael physical review | Signed dwell surplus in mission-gap results | Supported energy/power domain; this remains an energy proxy |
| R3 | Independent segment ledger and reserve equality/shortfall check | Noah calculation; Michael physical review | Numerical fixtures and full six-segment ledger | Physical power/usable-energy support and justified discrepancy |
| R4 | Installed mass summation and declared ceiling check | Noah | Component breakdown and mass gate tests | Evidence for selected installation and actual mass ceiling |
| R5 | Maximum segment bus-demand comparison | Noah interfaces; Michael demand model | Independent power-gate test and per-option surplus | Supply capability evidence; transients remain outside calculation |
| R6 | Inspect interface definitions, assumptions and evidence gaps | Noah | Typed registry, interface register and architecture acceptance | Physical compatibility evidence before implementation |
| R7 | Inspect six generated records for complete comparison fields | Noah / Codex | comparison.csv, baseline.json and baseline acceptance | Preserve the six-option record after reviewed changes; no flight claim |
| R8 | Reproduce outputs; compare input/source hashes and status | Noah / Codex | Resolved inputs, source provenance, extracted-archive check | Preserve provenance when actual reviewed changes are integrated |

The [mission gap table](../results/mission-gap.md) reports capability against fixed demand. The [MBSE method](mbse-method.md) explains why requirement intent, calculation verification, physical evidence and mission validation remain separate.
