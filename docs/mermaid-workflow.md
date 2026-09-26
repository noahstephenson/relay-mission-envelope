# Mermaid diagram workflow

How do Noah and Codex maintain the assembled views?

1. Open `Diagram_Book.html` for the rendered reading copy, or `docs/diagram-book.md` in a Mermaid-capable Markdown viewer.
2. Edit the relevant source in `diagrams/`. Its ID, title, explanatory caption and referenced model elements are listed in `diagrams/index.json`.
3. If meaning changes, update the matching elements or relationships in `model/architecture.json`. Keep the short presentation labels consistent with the detailed architecture tables.
4. Run `python scripts/reproduce.py` for calculations and model checks.
5. Render modified views with mermaid-cli 12.0.0, then inspect them:

```bash
python scripts/render_diagrams.py --mmdc /path/to/mmdc
```

Use the actual executable path on your machine. The rendering script rebuilds both books after generating SVG and PNG exports. Calculation reproduction itself does not need Node or the renderer. A browser-launch configuration may be passed with `--puppeteer-config` if your local environment requires one; do not copy environment-specific settings blindly.

## Notation

| View | Mermaid form | Interpretation |
|---|---|---|
| Requirements | Flowchart | Named needs/requirements; deriveReqt and verify-intent labels |
| Use cases | Flowchart with rounded nodes | Actor participation, not execution order |
| Activities | Flowchart | Nominal sequence and explicit supporting responsibilities |
| Block definitions | Class diagram | Composition and named part roles |
| Internal connections | Flowchart | Named component usages and typed power/data interactions |
| Lifecycle | State diagram | Intended operational states and transitions |
| Parametrics | Flowchart with undirected lines | Equality bindings and displayed equations; Python evaluates them |

Keep supporting prose outside diagrams. Use short labels, a top-down or shallow left-to-right layout, and no more than five nodes horizontally. Split a crowded view instead of shrinking its text. The books contain all current views; the JSON tables retain details that would clutter a drawing.

## Review acceptance

Check the need-to-requirement coverage, function allocations, composition, interface directions, reserve units and diagram labels. Confirm all views render and remain readable. Accepting the architecture does not validate hardware or Michael's pending physics. The current rendering and code checks are recorded in `docs/verification.md`.
