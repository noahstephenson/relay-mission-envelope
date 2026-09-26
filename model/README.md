# Architecture definitions and Mermaid views

`architecture.json` holds stable IDs, requirements, typed blocks/properties/interfaces and relationship definitions. `tables/` and `CATALOG.md` are generated inspection aids. `diagrams/` holds the complete editable Mermaid presentation.

```bash
python scripts/build_architecture.py
python scripts/build_diagram_book.py
```

The first script checks IDs, allocations, requirement verification intent, nested component paths, port compatibility and binding types. It also resolves property values for all six cases. The second assembles the diagram sources and existing exports into Markdown and offline HTML.

For an architecture change, update this registry and the affected Mermaid source together. Change numerical inputs only in `config/baseline.json`; regenerate calculations before exporting property tables. Keep IDs stable when labels change. Do not edit generated CSV values or calculation outputs to change the recommendation.

The registry checks consistency within this project; they do not certify formal SysML conformance. Detailed interface tables supplement intentionally simple diagrams.
