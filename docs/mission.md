# Mission and stakeholder needs

Who needs the relay, and what is the sortie expected to accomplish?

A fictional field team needs one-way communications from endpoint A to a remote logistics or aid endpoint B. An intervening wall screens the direct path. A multirotor carries a radio relay to a selected station, provides the requested service, and returns to its launch point with reserve.

| Need | Stakeholder | Need and measure |
|---|---|---|
| N1 | Field communications user | 900 s of service; two-hop clearance and link screen |
| N2 | Aircraft operator | Planned sortie plus reserve within available energy |
| N3 | Field support | Understand battery and installed mass burden |
| N4 | Engineering reviewer | Trace assumptions to repeatable results |

These needs are analyst-defined; no stakeholder interviews or approval are claimed. Positive hop margins do not demonstrate packet availability. Mass is only a partial measure of deployment burden.

## Operational thread
| Use case | Actor / trigger | Intended completion |
|---|---|---|
| UC1 Prepare | Operator receives service request | Select configuration and check planned mission |
| UC2 Establish | Operator dispatches aircraft | Climb, transit, establish both service hops |
| UC3 Sustain | Service begins | Deliver requested dwell |
| UC4 Recover | Dwell completes or service ends | Return horizontally, descend at base |
| UC5 Restore readiness | Field support receives aircraft | Battery/inspection responsibilities identified |

Normal operation is prepare → climb → transit → establish → relay → return → descend. In the exceptional planning case, inadequate recovery energy rejects an option before dispatch. Live contingency control and turnaround scheduling are outside the implementation.

## Scenario and boundary
All coordinates are local ENU meters with flat ground at z=0. Base=(0,0,0), A=(0,0,2), B=(1200,0,2). An infinitely thin wall spans north coordinates at east=600 m and rises to 35 m. The path screen requires another 5 m of straight-ray clearance; Fresnel clearance, diffraction and surveyed terrain are unmodeled.

The aircraft climbs vertically above base to station altitude, transits horizontally, establishes for 30 s, serves for 900 s, returns horizontally, and descends at base. The mission ledger includes all six airborne segments. Preparation and the supporting operator station are outside airborne energy accounting. Rotor geometry and atmosphere are fixed; wind is zero.

The system of interest includes aircraft, battery, relay payload and operator support. Endpoints, terrain and atmosphere are external. The carrier command/status link is distinct from service traffic and is assumed available; it is not assessed by the radio calculation.

## Noah's OV-1 brief
Show A, B, obstruction, relay aircraft and launch/recovery point. Distinguish service hops, carrier command/status, and outbound/return flight with three styles. Caption: “Establish temporary service, sustain the requested dwell, and recover with reserve.” Label terrain conceptual. Use the context view in [architecture](architecture.md) until the polished illustration is available.
