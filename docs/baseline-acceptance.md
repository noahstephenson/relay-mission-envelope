# Baseline acceptance

Date: 2026-09-26
Owner: Noah

Noah accepts the relay mission envelope baseline as the working architecture and trade-study scope for the next review stage.

## Accepted scope

- One fixed multirotor carrier with an installed relay payload.
- Two battery alternatives and three relay station alternatives, evaluated as six fixed options.
- Mission phases covering departure, establishment, relay service, return and recovery.
- Installed mass, propulsion power, auxiliary loads, usable energy, reserve, geometry and link checks as the bounded feasibility screen.
- A 900 s requested relay dwell remains the baseline mission demand.

## Accepted conventions

- The reserve convention is applied as usable energy after reserve, not as a second reserve subtraction.
- Every mission segment carries avionics and relay auxiliary load continuously.
- Battery choice changes installed mass and available energy; it does not change the mission, radio architecture or station geometry.
- The selector is deterministic and may return `NO_FEASIBLE_OPTION`; assumptions are not tuned to force a feasible winner.

## Baseline result

The accepted modeled baseline result is `NO_FEASIBLE_OPTION`. B2-S2 is the closest modeled energy case at about 14.85 min maximum energy-supported dwell, while B2-S1 has energy margin but fails the clearance/link screen. This is a useful architecture result: the modeled mission demand is slightly beyond the current six-option envelope.

## Evidence status

The numerical inputs remain illustrative. This acceptance freezes the systems-engineering baseline and decision framing; it does not validate hardware performance, flight behavior, battery data, propulsion coefficients or uncertainty bounds. Michael's issues 10-12 remain the physical review path.
