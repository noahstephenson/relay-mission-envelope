# Proposed system architecture

What must the relay system do, what implements it, and where do its resources cross boundaries?

This is one architecture with two battery configurations and three operating locations. The architecture is proposed; only the screening calculations are implemented. Noah's OV-1 can introduce the operational story without changing these allocations.

## 1. Context
The operator prepares and commands the sortie; the two endpoints exchange one-way service through the aircraft. Field support prepares the battery and payload. Terrain and atmosphere constrain the operation.



## 2. Functions
Deployment, service and recovery consume energy. Resource monitoring informs the intended service/recovery decision. These are operational functions, not implemented flight-control code.



## 3. Logical responsibilities
Composition means “contains,” not power flow. Mission management handles the plan and status; flight support positions and recovers the aircraft; relay service forwards traffic; energy support supplies the loads.



| Logical element | Functions | Physical allocation | Information needed |
|---|---|---|---|
| L1 Mission management | F1 plan, F4 monitor, F5 recover | Operator support, P3 | Request, position, remaining energy and service state |
| L2 Flight support | F2 deploy, F5 recover | P3,P4,P6 | Station, route and recovery command |
| L3 Relay service | F3 maintain service | P5 | Endpoint/radio setup and service enable |
| L4 Energy support | F6 supply power; supports F4 | P1,P2 | Load and stored-energy state |

## 4. Physical composition
| Element | Contents | Mass ownership / role |
|---|---|---|
| P1 | Selected battery | B1 or B2 pack mass and energy |
| P2 | Distribution and regulation | Shared distribution/mount category; bus loads |
| P3 | Avionics and carrier radio | 0.2 kg; 12 W auxiliary demand |
| P4 | Controllers, motors, rotors | 0.8 kg; propulsion reference-power model |
| P5 | Relay payload and antennas | 0.35 kg; 18 W after regulation |
| P6 | Airframe, landing gear, mounts | 1.4 kg structure plus shared distribution/mount allocation |
| Support | Operator station and procedures | Outside airborne mass and energy accounting |

Shared distribution and reference mounts total 0.25 kg across P2/P6. The calculation counts this combined category once; it does not invent a parts-level split. Total nonbattery mass is 3.0 kg. B2 adds 0.1 kg of mounting beyond that baseline.

## 5. Physical connections
Commands, power, mission traffic and mechanical support have different meanings. This is a proposed connection concept, not a verified wiring diagram. Avionics also require airframe support even though its mount is omitted for readability.



## 6. Mission decisions
The diagram describes intended behavior. The program evaluates a planned sortie; it does not implement live monitoring, faults or contingency control.


## Instantiated interface register
| ID | Source → destination | Item / unit | Proposed constraint | Failure implication | Evidence |
|---|---|---|---|---|---|
| I1 | P1 → P2 | DC energy Wh, power W, voltage V | 22.2 V nominal, ≤1400 W modeled | Power loss or mission energy shortfall | Assumed; voltage envelope/connector unassessed |
| I2 | P2 → P5 | Regulated electrical load W | 18 W load; 20 W bus at 90% efficiency; payload voltage TBD by hardware | Relay unavailable | Assumed load; actual regulator compatibility unassessed |
| I3 | P6 → P1/P5 | Mechanical support / kg | Total ≤5.5 kg; B2 mount +0.1 kg | Installation or flight infeasible | Mass accounting only; attachment/CG unassessed |
| I4 | A → P5 → B | One-way service / RF | 2.4 GHz; ≥10 dB above -90 dBm; clear modeled ray | Service screen fails | Calculated link; throughput/scheduling assumed |
| I5 | Operator ↔ P3 | Commands/status / messages | Operator controls launch, end-service and recovery | Loss of mission control | Described, performance unassessed |

## Battery configuration cards
| Property | B1 Standard | B2 Extended energy |
|---|---|---|
| Purpose | Lower installed mass | More stored energy |
| Battery mass | 1.0 kg | 1.7 kg |
| Extra mount | 0 kg | 0.1 kg |
| Gross mass | 4.0 kg | 4.8 kg |
| Nominal / usable energy | 220 / 198 Wh | 360 / 324 Wh |
| Reserve / mission allowance | 39.6 / 158.4 Wh | 64.8 / 259.2 Wh |
| Voltage basis | 22.2 V nominal | 22.2 V nominal |
| Mounting | Reference mount assumed | Reinforced mount increment assumed |
| Changed interfaces | I1, I3 | I1, I3 |
| Open evidence | Fit, discharge, CG, connector, voltage envelope | Same, including mount suitability |

Functional allocations are conceptual responsibilities. L1 is implemented by operator procedures plus avionics; L2 by avionics, propulsion and airframe; L3 by the relay assembly; L4 by battery and distribution. The evaluator computes planned resource sufficiency; none of these allocations implies real-time control software exists.

## Property ownership and unit contract
| Configuration path | Unit | Owner / interpretation |
|---|---|---|
| vehicle.nonbattery_mass_kg | kg | Sum of installed components except pack and extra mount |
| batteries[].battery_mass_kg, mount_delta_kg | kg | P1 pack / P6 incremental support |
| batteries[].nominal_energy_wh | Wh | P1 nominal energy before deductions |
| mission.usable_fraction, reserve_fraction | fraction | Available share, then withheld share of usable energy |
| physics.reference_power_w, reference_mass_kg | W, kg | Propulsion-only electrical operating point |
| vehicle.payload_load_w | W | P5 load after regulation |
| vehicle.regulator_efficiency | fraction | P2; payload bus demand = load / efficiency |
| vehicle.continuous_bus_limit_w | W | Assumed P1/P2 continuous ceiling |
| stations[].position_m | m ENU | Relay position on common ground datum |
| mission.dwell_s | s | Time actually providing service |

Example trace: N2 recoverability → R3 energy/reserve → F4/F5/F6 → L1/L2/L4 → P1/P2/P3/P4 → I1 → the ledger and reserve-boundary test. Energy supports recovery; it does not demonstrate physical recovery. The complete requirement trace is in [requirements](requirements.md).



## Complete visual architecture

All 17 Mermaid views are assembled in [the diagram book](diagram-book.md), with a rendered offline copy at [Diagram_Book.html](../Diagram_Book.html). Editable sources are in `diagrams/`. This page retains the detailed allocation, interface and configuration tables.
