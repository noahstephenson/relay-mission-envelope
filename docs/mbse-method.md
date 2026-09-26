# How the models support the decision

What does the mission require, what can each configuration support, and what evidence connects the two?

We use the supplied NotebookLM report as a secondary reading guide to Ali Koudri's *Model Based System Engineering: Theoretical Foundations*, First Edition, identified by Noah as published by John Wiley & Sons, Inc. The book itself was not supplied or independently checked. Its reported chapter/page references are therefore not treated as verified citations. The method below is our project application, not a claim to reproduce a prescribed method from the book.

## Two sides of the same engineering question

**Mission demands** are the declared needs and requirements: provide the requested service, account for deployment and recovery, retain reserve, and expose the deployment burden and evidence. These are choices to be agreed with Noah, not conclusions inferred from a favorable simulation.

**Calculated capabilities** are what the six candidate configurations support under the explicit assumptions: clearance, link margin, installed mass, segment powers, usable energy and maximum energy-supported dwell. An assumed capability remains provisional even when the calculation is internally correct.

The [generated gap review](../results/mission-gap.md) compares the two. It retains signed margins and failed options. B2-S2's near-boundary result is a useful question for Michael's physical evidence work; it is not a reason to adjust the mission until that option passes.

## Small model set and connections

| Engineering question | Authoritative material | Connection to the next step |
|---|---|---|
| Who needs what? | mission.md; N1–N4 | Needs motivate R1–R8 |
| What must happen? | F1–F6 and mission lifecycle | Functions allocate to L1–L4 |
| Who carries each responsibility? | Logical and physical architecture tables | Allocations identify physical resources and interfaces |
| What crosses boundaries? | I1–I5, internal IF6 and typed property tables | Units and measurement boundaries constrain the calculation |
| Which option meets the declared request? | baseline.json, evaluator, six-option results | Signed margins reveal gaps; selector follows one declared rule |
| Why trust the conclusion? | Requirement verification matrix and evidence records | Calculation checks, physical support and human acceptance stay distinct |

The 17 Mermaid views are reading views of this compact model set, not 17 independent models. The diagram book splits dense relationships for readability. The registry retains stable IDs; the configuration retains numerical inputs; scripts generate outputs and inspectable tables. Changes to architecture meaning update the registry and affected diagrams together. Numerical changes flow through the reproduction command rather than manual result edits.

## Verification, physical support and validation

- **Calculation/model verification:** check arithmetic, units, references, allocations, interfaces and boundary behavior. Existing tests and reproduction records provide bounded evidence of these checks.
- **Physical model support:** Michael determines applicability and discrepancy from suitable evidence. A hover fit alone does not support all flight segments.
- **Mission validation:** Noah reviews whether the declared scenario, measures and decision rule answer the intended stakeholder question. Real operational service or flight capability is not demonstrated by that review or by a diagram.

A verify relationship records responsibility. A passing software test records a particular check. Neither automatically demonstrates a system requirement or guarantees safe recovery.

## How we used the supplied report

| Report theme | Disposition here |
|---|---|
| Connect operational needs and physical limits | Adopted as the demand/capability comparison |
| Explicit allocation, typed interfaces and evidence | Adopted through the registry, trace and verification matrix |
| Keep each model tied to a question | Adopted; existing views reused |
| New range, hardware, pack, reserve and radio values | Not adopted; unsupported and inconsistent with the frozen baseline |
| Wind, voltage sag, thermal behavior and dynamic routing | Outside this project's scope |
| Formal checking, co-simulation and transformation infrastructure | Not required for this planned-sortie study |
| Scenario probabilities and a new numerical winner | Not used; source basis and reproducible calculations are absent |
| Guaranteed mission success | Rejected as beyond the available evidence |

## Focused architecture acceptance

Noah checks that needs lead to measurable requirements, every function has an allocation, exchanges have clear boundaries/units, and failed or unassessed requirements remain visible. Michael checks only his bounded physical questions. A change to a requirement or assumption is recorded explicitly, followed by regeneration and a before/after explanation. There is no additional platform or experimental campaign in this method.
