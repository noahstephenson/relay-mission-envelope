# Verification performed

What has actually been checked in this package?

On 2026-09-25, the expanded reproduction pipeline completed with **20 tests and eight scenario checks passing**. Six options, four plots, typed model tables and provenance records were regenerated. The prepared dimensionless-mass expression matched all six discrete dwell calculations; its analytic derivative matched independent central differences and recovered the ideal limiting stationary point.

| Check | Result | Scope |
|---|---|---|
| Independent six-segment energy arithmetic | Pass | W·s to Wh, auxiliaries, explicit return and reserve |
| Reserve equality and shortfall | Pass | Feasibility boundary, signed margins |
| Clear/blocked/equality/coplanar wall cases | Pass | Declared thin-wall straight-ray screen |
| Independent 1 km radio fixture | Pass | Free-space loss and link-margin arithmetic |
| Mass and power ceilings | Pass | Separate gates and heavier-pack demand |
| Selection order and no-feasible cases | Pass | Mass, energy, link and ID ordering |
| Invalid inputs and outside-domain states | Pass | Representative rejection behavior, not exhaustive schema validation |
| Exact power break-even | Pass | Energy gate changes immediately either side of analytic boundary |
| Model registry | Pass | Unique IDs, known references, allocations and verification intent |
| Typed model mutations | Pass | Wrong port direction, nested occurrence, binding type and verify direction rejected |
| Eight scenario cases | 8/8 pass | Frozen baseline plus explicitly labeled request/parameter mutations |
| 17 Mermaid views | Rendered and visually inspected | SVG and PNG exports readable; source hashes recorded |
| Four scientific plots | Visually inspected | Labels/legends readable; failed-link curves retained |
| Hardware and physical support | Not validated | No flight, fit, actual service or evidence-based uncertainty claim |

Records: `results/test-report.txt`, `acceptance-cases.json`, `model-validation.json`, `algebra-checks.json`, `diagram-rendering.json`, and `source-provenance.json`. The package does not invent a Git commit; source bytes are hashed directly. See the delivery check record for extracted-archive reproduction.

Mermaid rendering used mermaid-cli 12.0.0. `scripts/render_diagrams.py` is optional; the calculation pipeline does not require Node or a diagram renderer. The supplied browser launch configuration was environment-specific and is not a required user setting.

Noah accepted the assembled architecture in `docs/architecture-acceptance.md`. Michael's derivation review, physical evidence and uncertainty result remain open. A verify relation and a successful numerical fixture are distinct from a demonstrated system requirement.

The scenario fixtures deliberately encode the supplied baseline and its expected results. If a reviewed change alters mission assumptions, preserve the prior outputs and update the relevant fixtures with a documented reason. Do not tune the baseline to satisfy a preferred result.

The Mermaid source set covers all seventeen views listed in `diagrams/index.json`. Each source was rendered successfully to SVG and PNG and visually inspected. Source hashes connect exports to the assembled Markdown and offline HTML book. These are SysML-style representations, not a formal semantic validation.

The offline HTML book contains seventeen embedded SVGs with unique IDs and no external asset dependencies. Individual exported views were visually inspected. A full browser preview of the combined book was unavailable in this environment; its document structure was checked directly.
