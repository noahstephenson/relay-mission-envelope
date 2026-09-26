# Relay mission envelope — diagram book

SysML-style views expressed in Mermaid. These are readable architecture diagrams, not a formal SysML execution model. Numerical values come from the configuration and Python calculations; physical evidence remains provisional.

## Reading order

| View | Diagram | Purpose |
|---|---|---|
| D01 | Mission context | Operational context |
| D02 | Service requirements | Requirement view |
| D03 | Recovery requirements | Requirement view |
| D04 | Interface and evidence requirements | Requirement view |
| D05 | Operational use cases | Use-case view |
| D06 | Mission functions | Activity-style view |
| D07 | Logical blocks | Block-definition-style view |
| D08 | Physical composition | Block-definition-style view |
| D09 | Airborne interfaces | Internal-block-style view |
| D10 | Service and carrier interfaces | Internal-block-style view |
| D11 | Mission lifecycle | State-machine view |
| D12 | Installed mass constraint | Parametric-style view |
| D13 | Energy and reserve constraint | Parametric-style view |
| D14 | Supported dwell constraint | Parametric-style view |
| D15 | Configuration decision | Activity-style analysis view |
| D16 | Propulsion power constraint | Parametric-style view |
| D17 | Segment energy constraint | Parametric-style view |

## D01 — Mission context

A-to-B service crosses the relay aircraft. Carrier command/status is a separate path; terrain constrains the service geometry.

```mermaid
flowchart TD
    A["Endpoint A"] -->|"Service traffic"| U["Relay aircraft"]
    U -->|"Relayed traffic"| B["Endpoint B"]
    O["Operator support"] <-->|"Carrier command and status"| U
    S["Field support"] -->|"Battery and payload preparation"| U
    E["Terrain and atmosphere"] -.->|"Geometry and operating conditions"| U
```

## D02 — Service requirements

Engineering requirements derive from the service need. Dashed verify links identify check responsibilities; they do not claim demonstrated communications performance.

```mermaid
flowchart TD
    N1["N1 Sustained service"]
    R1["R1 Clear paths and adequate link margin"] -->|"deriveReqt"| N1
    R2["R2 Required energy-supported dwell"] -->|"deriveReqt"| N1
    TC1["TC1 Geometry and radio checks"] -.->|"verify intent"| R1
    TC2["TC2 Dwell threshold check"] -.->|"verify intent"| R2
    P5["P5 Relay assembly"] -.->|"responsibility trace"| R1
    P1["P1 Battery"] -.->|"resource trace"| R2
```

## D03 — Recovery requirements

Energy, installed mass and continuous demand constrain the planned sortie. Thresholds remain illustrative and actual recovery has not been demonstrated.

```mermaid
flowchart TD
    R3["R3 Mission energy plus reserve"] -->|"deriveReqt"| N2["N2 Recoverable sortie"]
    R4["R4 Gross mass ceiling"] -->|"deriveReqt"| N2
    R5["R5 Continuous bus limit"] -->|"deriveReqt"| N2
    TC3["TC3 Ledger and reserve boundary"] -.->|"verify intent"| R3
    TC4["TC4 Installed mass check"] -.->|"verify intent"| R4
    TC5["TC5 Segment power check"] -.->|"verify intent"| R5
```

## D04 — Interface and evidence requirements

Installation evidence, comparison records and reproducibility have different checks. The interface review remains open even when the numerical tests pass.

```mermaid
flowchart TD
    R6["R6 Declared installation interfaces"] -->|"deriveReqt"| N2["N2 Recoverable sortie"]
    R6 -.->|"trace"| N3["N3 Deployment burden"]
    R7["R7 Six comparable option records"] -->|"deriveReqt"| N3
    R8["R8 Reproducible provenance"] -->|"deriveReqt"| N4["N4 Reviewable recommendation"]
    TC6["TC6 Human interface review"] -.->|"verify intent"| R6
    TC7["TC7 Output inspection"] -.->|"verify intent"| R7
    TC8["TC8 Hash and reproduction checks"] -.->|"verify intent"| R8
```

## D05 — Operational use cases

Rounded nodes represent use cases. Actor associations express participation, not execution order. Restore readiness is described but not simulated.

```mermaid
flowchart TD
    A2["Aircraft operator"] --- UC1(["UC1 Prepare sortie"])
    A2 --- UC2(["UC2 Establish service"])
    A2 --- UC4(["UC4 Recover aircraft"])
    A1["Communications user"] --- UC3(["UC3 Sustain service"])
    A3["Field support"] --- UC5(["UC5 Restore readiness"])
    subgraph SYS["Deployable relay capability"]
      UC1
      UC2
      UC3
      UC4
      UC5
    end
```

## D06 — Mission functions

Solid arrows indicate the nominal function sequence. Dashed arrows indicate supporting responsibilities, avoiding the suggestion that monitoring and power are extra timed flight segments.

```mermaid
flowchart TD
    F1["F1 Plan and configure"] --> F2["F2 Deploy and position"]
    F2 --> F3["F3 Maintain relay service"]
    F3 --> F5["F5 Return and recover"]
    F4["F4 Monitor resources and status"] -.->|"Continue or end service"| F3
    F4 -.->|"Recovery decision"| F5
    F6["F6 Supply and distribute power"] -.-> F2
    F6 -.-> F3
    F6 -.-> F4
    F6 -.-> F5
```

## D07 — Logical blocks

Composition groups responsibilities independently of hardware. Class compartments list responsibilities, not implemented software methods.

```mermaid
classDiagram
    direction TB
    class L0["Relay capability"]
    class L1["L1 Mission management"] {
      Plan and configure
      Assess status and recovery
    }
    class L2["L2 Flight support"] {
      Deploy and position
      Return and recover
    }
    class L3["L3 Relay service"] {
      Receive mission traffic
      Forward mission traffic
    }
    class L4["L4 Energy support"] {
      Store and distribute energy
      Provide resource information
    }
    L0 *-- L1 : mission
    L0 *-- L2 : flight
    L0 *-- L3 : service
    L0 *-- L4 : energy
```

## D08 — Physical composition

Composition shows owned physical groups. Each box is a reusable block type; the labeled relationship is the part role. Both battery choices use this same structure.

```mermaid
classDiagram
    direction LR
    class SYS["Deployable relay system"]
    class AIR["Relay aircraft"]
    class OP["Operator support"]
    class P1["P1 Battery"]
    class P2["P2 Distribution and regulation"]
    class P3["P3 Avionics and carrier radio"]
    class P4["P4 Propulsion assembly"]
    class P5["P5 Relay assembly"]
    class P6["P6 Airframe and mounts"]
    SYS *-- AIR : aircraft
    SYS *-- OP : operatorSupport
    AIR *-- P1 : battery
    AIR *-- P2 : distribution
    AIR *-- P3 : avionics
    AIR *-- P4 : propulsion
    AIR *-- P5 : relay
    AIR *-- P6 : structure
```

## D09 — Airborne interfaces

Solid edges carry electrical supply; the dashed edge carries flight commands. Interface types and conjugated port directions remain explicit in the model tables.

```mermaid
flowchart TD
    P1["battery: P1"] -->|"I1 Main DC supply"| P2["distribution: P2"]
    P2 -->|"I1 Propulsion supply"| P4["propulsion: P4"]
    P2 -->|"I1 Avionics supply"| P3["avionics: P3"]
    P2 -->|"I2 Regulated payload supply"| P5["relay: P5"]
    P3 -.->|"IF6 Flight commands"| P4
```

## D10 — Service and carrier interfaces

The served endpoints are external. Mission traffic and carrier control enter different aircraft responsibilities; no throughput or command-link reliability is demonstrated here.

```mermaid
flowchart TD
    EA["Endpoint A"] -->|"I4 Service hop 1"| P5["relay: P5"]
    P5 -->|"I4 Service hop 2"| EB["Endpoint B"]
    OP["operatorSupport: OP"] -->|"I5 Carrier commands"| P3["avionics: P3"]
    P3 -->|"I5 Aircraft status"| OP
    subgraph AIR["Aircraft boundary"]
      P5
      P3
    end
```

## D11 — Mission lifecycle

The diagram specifies intended operational decisions. The evaluator checks a planned sortie and does not implement live flight control or off-nominal recovery.

```mermaid
stateDiagram-v2
    [*] --> Preflight
    Preflight --> Deploy: Preparation accepted
    Preflight --> NoDispatch: Gate fails or evidence missing
    Deploy --> Relay: Station established
    Deploy --> Recover: Establishment unsuccessful
    Relay --> Recover: Dwell complete or service ends
    Recover --> Complete: Recovery completed
    NoDispatch --> [*]
    Complete --> [*]
```

## D12 — Installed mass constraint

Undirected lines mean equality bindings between named values and constraint parameters. The mount increment is separate from pack mass. Python evaluates the relation.

```mermaid
flowchart TD
    MD["nonbatteryMass: kg"] ---|"nonbattery"| CB1["CB1 GrossMass: gross = nonbattery + battery + mount"]
    MB["batteryMass: kg"] ---|"battery"| CB1
    MM["mountIncrement: kg"] ---|"mount"| CB1
    CB1 ---|"gross"| MG["grossMass: kg"]
```

**Constraint:** gross = nonbattery + battery + mount

## D13 — Energy and reserve constraint

One reserve deduction is applied to usable energy. Binding lines state equality, not calculation order; the constraint expression is listed below the figure in the book.

```mermaid
flowchart LR
    subgraph INPUT["Case values"]
      EN["nominalEnergy: Wh"]
      U["usableFraction: 1"]
      R["reserveFraction: 1"]
      EM["missionEnergy: Wh"]
    end
    EN ---|"nominal"| CB4["CB4 ReserveAccounting"]
    U ---|"usableFraction"| CB4
    R ---|"reserveFraction"| CB4
    EM ---|"mission"| CB4
    CB4 ---|"usable"| EU["usableEnergy: Wh"]
    CB4 ---|"reserve"| ER["reserveEnergy: Wh"]
    CB4 ---|"margin"| M["energyMargin: Wh"]
```

**Constraint:** usable = nominal × usableFraction; reserve = usable × reserveFraction; margin = usable − reserve − mission

## D14 — Supported dwell constraint

The maximum energy-supported dwell retains its sign. A negative value means the nonservice sortie already exceeds the allowance. Radio, mass and power checks still apply.

```mermaid
flowchart LR
    subgraph VALUES["Case values"]
      U["usableEnergy: Wh"]
      R["reserveEnergy: Wh"]
      Q["nonserviceEnergy: Wh"]
      P["servicePower: W"]
    end
    U ---|"usable"| CB5["CB5 EnergySupportedDwell"]
    R ---|"reserve"| CB5
    Q ---|"nonservice"| CB5
    P ---|"servicePower"| CB5
    CB5 ---|"dwell"| T["maximumDwell: s"]
```

**Constraint:** dwell = (usable − reserve − nonservice) × 3600 / servicePower

## D15 — Configuration decision

Six options share one mission and requirement basis. The selection is provisional and never converts missing hardware or physical evidence into a pass.

```mermaid
flowchart TD
    B["Two battery configurations"] --> E["Evaluate all six options"]
    S["Three relay stations"] --> E
    M["Shared mission and assumptions"] --> E
    E -.-> X["Report every option and failure reason"]
    E --> G{"Any option passes modeled gates and domain?"}
    G -->|"No"| N["No feasible option in this model"]
    G -->|"Yes"| W["Select lowest mass; then energy, link margin and ID"]
```

## D16 — Propulsion power constraint

Fixed rotor geometry and a propulsion-only reference operating point define the provisional hover electrical law. The shared multiplier is a sensitivity input, not a wind model.

```mermaid
flowchart LR
    G["grossMass: kg"] ---|"gross"| CB2["CB2 HoverElectricalPower"]
    RM["referenceMass: kg"] ---|"referenceMass"| CB2
    RP["referencePower: W"] ---|"referencePower"| CB2
    A["powerMultiplier: 1"] ---|"multiplier"| CB2
    CB2 ---|"hover"| P["hoverPower: W"]
```

**Constraint:** hover = referencePower × (gross / referenceMass)^1.5 × multiplier

## D17 — Segment energy constraint

Propulsion and auxiliary loads are accounted at the main bus. The payload regulator loss enters once. Duration times power is converted from joules to Wh by dividing by 3600.

```mermaid
flowchart TD
    H["hoverPower: W"] --- BUS["busPower = hoverPower x segmentFactor + auxiliaryPower"]
    K["segmentFactor: 1"] --- BUS
    AUX["auxiliaryPower = avionics + payload / efficiency"] --- BUS
    BUS ---|"busPowerW"| CB3["CB3 SegmentEnergy"]
    T["segmentDuration: s"] ---|"durationSeconds"| CB3
    CB3 ---|"energyWh"| E["segmentEnergy: Wh"]
```

**Constraint:** busPower = hover × segmentFactor + avionics + payload / efficiency; energyWh = busPower × durationSeconds / 3600

## Notation and limits

Composition diamonds appear in the block-style class diagrams. Requirement arrows labeled deriveReqt point to the parent need. Verify links express check intent. Undirected parametric lines denote equality bindings; they are not execution arrows. Diagram labels summarize the registry and tables, which retain detailed properties and typed interfaces.

The activity-style decision view summarizes a batch comparison; it does not implement flight control. Read docs/architecture.md for allocations, mounting relationships and interface evidence.
