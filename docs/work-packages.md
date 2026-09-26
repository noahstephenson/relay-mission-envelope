# Work packages and handoff

Which packages are complete, and what remains?

The implemented calculation and model registry are the starting baseline. These work packages close specific remaining gaps. They do not authorize a new platform or broader research program.

## WP1 — Noah accepts the mission and architecture

**Inputs:** mission, architecture, requirements, decision log and generated decision brief.

**Already prepared:** four stakeholder needs, five use cases, six functions, four logical responsibilities, six airborne physical groups, five top-level interfaces and a six-option comparison.

**Accepted:** Noah reviewed the scenario, boundaries, reserve and selector. Illustrative hardware remains conceptual, and the modeled result does not claim operational performance.

**Return:** completed in `docs/baseline-acceptance.md`, naming accepted choices and outstanding evidence.

**Exit:** complete. Architecture is explainable and scope is fixed. Michael's physical validation and the optional polished overview remain separate.

## WP2 — Noah reviews the assembled Mermaid views

**Inputs:** `Diagram_Book.html`, `docs/diagram-book.md`, `diagrams/` and model tables.

**Already built:** 17 SysML-style views covering the complete intended architecture, with editable sources and SVG/PNG exports. Requirements, use cases, functions, block composition, interfaces, states, constraints and decision logic are assembled.

**Accepted:** Noah reviewed the book and accepted the architecture. Future changes to architecture meaning should update affected sources and registry records together.

**Return:** completed in `docs/architecture-acceptance.md`.

**Exit:** complete. Noah accepts the architecture baseline independently of Michael's physics work.

## WP3 — Noah supplies the polished operational view

**Inputs:** mission/OV-1 brief and rendered context view.

**Already prepared:** system boundary, endpoint names, conceptual obstacle, service/control/flight distinctions.

**Do:** create a clear overview using the same mission labels. Show concept rather than surveyed terrain. Keep technical tables out of the graphic.

**Return:** an editable source plus publication-quality export and one caption. Link it in README and mission documentation.

**Exit:** a first-time reader can explain why the relay exists and why return energy matters. No DoDAF profile or new model element is required.

## WP4 — Michael derives the admitted physical boundary

**Inputs:** `physics/analytical_starter.py`, physics packet, boundary outputs, issue 10.

**Already prepared:** energy balance, mass/power normalization, derivative, limiting case and numerical equivalence for all six options.

**Do:** verify/correct assumptions; normalize time explicitly; establish the allowed mass interval; solve the scalar stationary condition and compare constraint endpoints; distinguish each real pack from a hypothetical constant-specific-energy family.

**Return:** reviewed derivation plus corrected script and a short physical explanation. Identify assistance versus Michael's actual analysis.

**Exit:** the physical mechanism and constrained rather than purely mathematical optimum are clear. Stop at one reduced-order model.

## WP5 — Michael establishes support and discrepancy

**Inputs:** assumption register, candidate primary sources and evidence-table schema, issue 11.

**Already prepared:** exact reference-power boundary, installed masses, component grouping, segment factors and open-source candidates.

**Do:** use a small appropriate public source set; state whether data calibrate or independently check the model; bound discrepancy only where warranted; identify mass, power and operating-state limits. Keep climb/transit/descent allowances separate from hover evidence.

**Return:** populated evidence/correction table and supported/unsupported domain statement.

**Exit:** the reader knows which physical claims are supported and which remain assumptions. If evidence is insufficient, narrow the claim instead of collecting a new dataset.

## WP6 — Michael explains decision uncertainty

**Inputs:** WP4/WP5, shared-power sensitivity, analytical break-even table, issue 12.

**Already prepared:** deterministic selector and fixed-geometry power/energy boundaries; tests immediately either side of the critical multiplier.

**Do:** derive sensitivities to dominant parameters; select evidence-based bounds; establish extrema or state why unresolved; apply common parameter realizations across alternatives; prepare one figure distinguishing admitted, rejected and unresolved regions.

**Return:** one figure, checked derivative/bound calculations and whether the recommendation is stable, changes or cannot be resolved. Do not label an arbitrary ±10% interval a probability distribution.

**Exit:** the physical result explains the configuration decision. A null or unresolved result is acceptable.

## WP7 — Noah/Codex integrates and assesses the submission

**Inputs:** actual Michael handback, accepted architecture, source provenance and issue 13.

**Already prepared:** reproducible pipeline, baseline result, issue bodies and submission outline.

**Do:** preserve the earlier baseline; apply only justified changes; rerun; update Mermaid property values and relevant constraints; write the before/after explanation and bounded contribution claim. Compare against earlier relay work before drafting a submission.

**Return:** updated result, accepted model, concise technical narrative and publication/case-study decision.

**Exit:** numbers, diagrams and claims agree. No specific venue is required to complete the engineering work.


## Review addition from the reading report

WP1 uses `docs/mbse-method.md`, the R1–R8 verification matrix, and generated `results/mission-gap.md`. Confirm the mission demands independently of the computed outcome; then review the signed capability gaps. This adds no new physics assignment or system feature.

