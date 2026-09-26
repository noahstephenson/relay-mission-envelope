# Design decisions and unresolved choices

Why is the project structured this way?

| Decision | Chosen approach | Reason | Revisit only if |
|---|---|---|---|
| Scope | One architecture, two packs, three stations | Small comparison with understandable physical trade | Mission owner changes the research question |
| Route | Sequential vertical/horizontal segments | Explicit accounting; avoids double-counting simultaneous motion | Michael provides a bounded alternative with consistent ledger |
| Power | Reference electrical propulsion law plus separate auxiliaries | Transparent load boundary | Evidence supports a corrected relation |
| Reserve | Fraction of usable energy withheld once | Direct compatibility with analytic model | A supported operational convention requires a coordinated update |
| Selection | Lowest mass feasible, then energy margin, link margin, ID | Reproducible rule without arbitrary scores | Noah deliberately revises decision preference |
| Geometry | Thin wall plus free-space budget | A clear, bounded station screen | A real terrain/service question warrants a different project |
| Baseline outcome | Preserve no-feasible-option at 900 s | Near-boundary result is informative | Evidence changes inputs; do not tune for a winner |
| Diagram notation | SysML-style Mermaid views | Simple, editable and readable in one book | A specific view becomes too crowded |
| Model detail | JSON registry and generated inspection tables | Preserve IDs and typed details behind simple views | Architecture meaning changes |
| Review | Noah accepts architecture; Michael owns physical evidence | Contributions remain distinct and manageable | Team explicitly changes responsibilities |

Open numerical evidence belongs in `docs/assumptions.md`. Open implementation/acceptance work belongs in `docs/issues.md`. Do not turn either into an unbounded research queue.
