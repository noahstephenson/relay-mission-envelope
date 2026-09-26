# Model catalog

Generated from `model/architecture.json`; edit the JSON and rebuild. The complete visual architecture is assembled in docs/diagram-book.md.

| ID | Name | Type | Package |
|---|---|---|---|
| A1 | Field communications user | Actor | PK1 |
| A2 | Aircraft operator | Actor | PK1 |
| A3 | Field support | Actor | PK1 |
| A4 | Engineering reviewer | Actor | PK1 |
| N1 | Sustained service | Requirement | PK1 |
| N2 | Recoverable sortie | Requirement | PK1 |
| N3 | Deployment burden | Requirement | PK1 |
| N4 | Reviewable recommendation | Requirement | PK1 |
| UC1 | Prepare relay sortie | UseCase | PK1 |
| UC2 | Establish service | UseCase | PK1 |
| UC3 | Sustain relay service | UseCase | PK1 |
| UC4 | End service and recover | UseCase | PK1 |
| UC5 | Restore readiness | UseCase | PK1 |
| R1 | Clear and adequate service hops | Requirement | PK2 |
| R2 | Requested service duration | Requirement | PK2 |
| R3 | Mission energy and reserve | Requirement | PK2 |
| R4 | Gross mass ceiling | Requirement | PK2 |
| R5 | Continuous bus power | Requirement | PK2 |
| R6 | Declared installation interfaces | Requirement | PK2 |
| R7 | Comparable alternative records | Requirement | PK2 |
| R8 | Reproducible provenance | Requirement | PK2 |
| F1 | Plan and configure | Activity | PK3 |
| F2 | Deploy and position | Activity | PK3 |
| F3 | Maintain relay service | Activity | PK3 |
| F4 | Monitor resources and status | Activity | PK3 |
| F5 | Return and recover | Activity | PK3 |
| F6 | Supply and distribute power | Activity | PK3 |
| ACT0 | Relay mission thread | Activity | PK3 |
| SM1 | Mission lifecycle | StateMachine | PK3 |
| L0 | Relay logical capability | Block | PK4 |
| L1 | Mission management | Block | PK4 |
| L2 | Flight support | Block | PK4 |
| L3 | Relay service | Block | PK4 |
| L4 | Energy support | Block | PK4 |
| CTX | Mission context | Block | PK5 |
| SYS | Deployable relay system | Block | PK5 |
| AIR | Relay aircraft | Block | PK5 |
| P1 | Battery | Block | PK5 |
| P2 | Distribution and regulation | Block | PK5 |
| P3 | Avionics and carrier radio | Block | PK5 |
| P4 | Propulsion assembly | Block | PK5 |
| P5 | Relay assembly | Block | PK5 |
| P6 | Airframe and mounts | Block | PK5 |
| OP | Operator support | Block | PK5 |
| EA | Field endpoint A | Block | PK5 |
| EB | Remote endpoint B | Block | PK5 |
| ENV | Environment | Block | PK5 |
| VT1 | Mass | ValueType | PK6 |
| VT2 | Power | ValueType | PK6 |
| VT3 | Energy | ValueType | PK6 |
| VT4 | Duration | ValueType | PK6 |
| VT5 | Length | ValueType | PK6 |
| VT6 | Voltage | ValueType | PK6 |
| VT7 | Fraction | ValueType | PK6 |
| VT8 | Frequency | ValueType | PK6 |
| VT9 | Decibel | ValueType | PK6 |
| VT10 | Speed | ValueType | PK6 |
| VT11 | Count | ValueType | PK6 |
| VT12 | PowerLevel | ValueType | PK6 |
| IT1 | MissionTraffic | DataType | PK6 |
| IT2 | CarrierCommand | DataType | PK6 |
| IT3 | CarrierStatus | DataType | PK6 |
| IT4 | FlightCommand | DataType | PK6 |
| I1 | MainBusSupply | InterfaceBlock | PK6 |
| I2 | PayloadSupply | InterfaceBlock | PK6 |
| I3 | MechanicalSupport | InterfaceBlock | PK6 |
| I4 | RelayTraffic | InterfaceBlock | PK6 |
| I5 | CarrierControl | InterfaceBlock | PK6 |
| IF6 | FlightControl | InterfaceBlock | PK6 |
| CASE | MissionAnalysisCase | Block | PK7 |
| CB1 | GrossMass | ConstraintBlock | PK7 |
| CB2 | HoverElectricalPower | ConstraintBlock | PK7 |
| CB3 | SegmentEnergy | ConstraintBlock | PK7 |
| CB4 | ReserveAccounting | ConstraintBlock | PK7 |
| CB5 | EnergySupportedDwell | ConstraintBlock | PK7 |
| TC1 | Verify R1 | TestCase | PK8 |
| TC2 | Verify R2 | TestCase | PK8 |
| TC3 | Verify R3 | TestCase | PK8 |
| TC4 | Verify R4 | TestCase | PK8 |
| TC5 | Verify R5 | TestCase | PK8 |
| TC6 | Verify R6 | TestCase | PK8 |
| TC7 | Verify R7 | TestCase | PK8 |
| TC8 | Verify R8 | TestCase | PK8 |

## Diagram inventory

| ID | View | Owner | Purpose |
|---|---|---|---|
| D01 | Mission context | PK0 | A-to-B service crosses the relay aircraft. Carrier command/status is a separate path; terrain constrains the service geometry. |
| D02 | Service requirements | PK0 | Engineering requirements derive from the service need. Dashed verify links identify check responsibilities; they do not claim demonstrated communications performance. |
| D03 | Recovery requirements | PK0 | Energy, installed mass and continuous demand constrain the planned sortie. Thresholds remain illustrative and actual recovery has not been demonstrated. |
| D04 | Interface and evidence requirements | PK0 | Installation evidence, comparison records and reproducibility have different checks. The interface review remains open even when the numerical tests pass. |
| D05 | Operational use cases | PK0 | Rounded nodes represent use cases. Actor associations express participation, not execution order. Restore readiness is described but not simulated. |
| D06 | Mission functions | PK0 | Solid arrows indicate the nominal function sequence. Dashed arrows indicate supporting responsibilities, avoiding the suggestion that monitoring and power are extra timed flight segments. |
| D07 | Logical blocks | PK0 | Composition groups responsibilities independently of hardware. Class compartments list responsibilities, not implemented software methods. |
| D08 | Physical composition | PK0 | Composition shows owned physical groups. Each box is a reusable block type; the labeled relationship is the part role. Both battery choices use this same structure. |
| D09 | Airborne interfaces | PK0 | Solid edges carry electrical supply; the dashed edge carries flight commands. Interface types and conjugated port directions remain explicit in the model tables. |
| D10 | Service and carrier interfaces | PK0 | The served endpoints are external. Mission traffic and carrier control enter different aircraft responsibilities; no throughput or command-link reliability is demonstrated here. |
| D11 | Mission lifecycle | PK0 | The diagram specifies intended operational decisions. The evaluator checks a planned sortie and does not implement live flight control or off-nominal recovery. |
| D12 | Installed mass constraint | PK0 | Undirected lines mean equality bindings between named values and constraint parameters. The mount increment is separate from pack mass. Python evaluates the relation. |
| D13 | Energy and reserve constraint | PK0 | One reserve deduction is applied to usable energy. Binding lines state equality, not calculation order; the constraint expression is listed below the figure in the book. |
| D14 | Supported dwell constraint | PK0 | The maximum energy-supported dwell retains its sign. A negative value means the nonservice sortie already exceeds the allowance. Radio, mass and power checks still apply. |
| D15 | Configuration decision | PK0 | Six options share one mission and requirement basis. The selection is provisional and never converts missing hardware or physical evidence into a pass. |
| D16 | Propulsion power constraint | PK0 | Fixed rotor geometry and a propulsion-only reference operating point define the provisional hover electrical law. The shared multiplier is a sensitivity input, not a wind model. |
| D17 | Segment energy constraint | PK0 | Propulsion and auxiliary loads are accounted at the main bus. The payload regulator loss enters once. Duration times power is converted from joules to Wh by dividing by 3600. |
