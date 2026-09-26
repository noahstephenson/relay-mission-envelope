# Start here

The architecture diagrams are assembled. The package uses Mermaid throughout; there is no separate modeling-tool assembly step.

## Read the completed architecture

| File | Use |
|---|---|
| [Diagram_Book.html](Diagram_Book.html) | Open locally for all 17 rendered views, explanations and expandable Mermaid source |
| [docs/diagram-book.md](docs/diagram-book.md) | Same views as Mermaid code blocks in Markdown |
| `diagrams/*.mmd` | Authoritative editable diagram sources |
| `assets/diagrams/` | SVG and PNG exports |
| [docs/architecture.md](docs/architecture.md) | Allocations, interfaces, mounting responsibilities and battery cards |
| [model/CATALOG.md](model/CATALOG.md) | Typed element and relationship inventory |
| [docs/completion-report.md](docs/completion-report.md) | Current implementation, verification results, limitations and handoff |

The views are SysML-style, expressed with Mermaid flowcharts, class diagrams and state diagrams. Labeled relationships explain their meaning. They are not a formal SysML execution model.

## Reproduce

```bash
python -m pip install -e .
python scripts/reproduce.py
```

On 2026-09-26 this completed on Windows after making generated text writes explicit UTF-8: 20 unit tests passed, eight acceptance cases passed, the six-option study regenerated, algebra checks ran, the architecture registry validated, and the 17-view diagram book assembled. Included SVG/PNG exports are already rendered. To change diagrams, follow [the Mermaid workflow](docs/mermaid-workflow.md); re-rendering uses mermaid-cli 12.0.0.

## What remains

Noah's mission, architecture, requirements and baseline acceptance are complete for repository handoff. Michael reviews and advances the prepared physical derivation, establishes evidence/domain limits, and quantifies decision uncertainty. Read [baseline acceptance](docs/baseline-acceptance.md), [architecture acceptance](docs/architecture-acceptance.md), [Noah completion](docs/noah-completion.md), [work packages](docs/work-packages.md), [issues](docs/issues.md), and [completion report](docs/completion-report.md).

The baseline retains its no-feasible-option result at 900 s; do not tune assumptions to manufacture a winner. No remote issues or submission have been created.

## Give Codex this instruction

> Continue from the implemented repository. Read START_HERE.md, docs/architecture.md, docs/work-packages.md, docs/verification.md and docs/completion-report.md. Open the assembled diagram book. Run `python scripts/reproduce.py`. Preserve the six-option scope and illustrative provenance. Keep all architecture diagrams in Mermaid; edit sources under diagrams/, render, then rebuild the diagram book. Check labels and IDs against model/architecture.json. Use Noah's acceptance docs as the closed architecture baseline. Michael's issues 10-12 remain his physical contribution; prepared algebra and figures are assistance. Do not rebuild the architecture, add another modeling platform or return another roadmap. Report actual edits, checks and remaining work.

Read [the MBSE method](docs/mbse-method.md) for the filtered application of the supplied reading report, and [mission demand versus capability](results/mission-gap.md) for the generated six-option gap review. The requirement page assigns verification methods, owners, evidence and closure criteria for R1-R8.

