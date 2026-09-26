# relay-mission-envelope

Which battery and relay station can provide temporary communications and still bring the aircraft home with reserve?

This repository contains the accepted Noah systems-engineering baseline: a Mermaid architecture package, a reproducible six-option analysis, and Michael's prepared physics handoff. All numerical inputs remain illustrative until Michael completes the physical evidence and uncertainty review.

**Open [Diagram_Book.html](Diagram_Book.html)** for the complete offline reading copy. The [Markdown diagram book](docs/diagram-book.md) contains the same 17 views as editable Mermaid code blocks. Individual `.mmd`, SVG and PNG files are included.

These are SysML-style views: requirements, use cases, activities, block definitions, interfaces, states and parametric constraints. Mermaid provides the readable notation; it does not enforce formal SysML semantics or execute constraints.

**Current baseline:** no option meets all modeled gates at 15 minutes. B2-S2 supports about 14.85 minutes; B2-S1 has energy but fails clearance. Read the [decision brief](results/decision-brief.md), [baseline acceptance](docs/baseline-acceptance.md), and [Noah completion note](docs/noah-completion.md).

```bash
python -m pip install -e .
python scripts/reproduce.py
```

Start with [START_HERE.md](START_HERE.md). Noah's mission, architecture, requirements, verification framing and handoff are complete for repository tracking. Michael owns the [three bounded physics assignments](docs/physics-review.md). The general goal remains a concise technical case study, with a research submission considered only if the completed physical result supports one.

Read [the MBSE method](docs/mbse-method.md) for the filtered application of the supplied reading report, and [mission demand versus capability](results/mission-gap.md) for the generated six-option gap review. The requirement page assigns verification methods, owners, evidence and closure criteria for R1-R8.
