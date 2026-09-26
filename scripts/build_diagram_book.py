"""Assemble the complete Mermaid source book and an offline rendered reading copy."""
import json,html,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def build():
    views=json.loads((ROOT/'diagrams/index.json').read_text(encoding='utf-8'))
    model=json.loads((ROOT/'model/architecture.json').read_text(encoding='utf-8'))
    known={x['id'] for x in model['elements']};ids=set()
    intro='SysML-style views expressed in Mermaid. These are readable architecture diagrams, not a formal SysML execution model. Numerical values come from the configuration and Python calculations; physical evidence remains provisional.'
    md=['# Relay mission envelope — diagram book','',intro,'','## Reading order','', '| View | Diagram | Purpose |','|---|---|---|']
    for v in views:md.append(f"| {v['id']} | {v['name']} | {v['kind']} |")
    pages=[];checks=[]
    eq={'D12':'gross = nonbattery + battery + mount','D13':'usable = nominal × usableFraction; reserve = usable × reserveFraction; margin = usable − reserve − mission','D14':'dwell = (usable − reserve − nonservice) × 3600 / servicePower','D16':'hover = referencePower × (gross / referenceMass)^1.5 × multiplier','D17':'busPower = hover × segmentFactor + avionics + payload / efficiency; energyWh = busPower × durationSeconds / 3600'}
    for v in views:
        assert v['id'] not in ids;ids.add(v['id']);assert set(v['element_ids'])<=known
        source=(ROOT/v['source']).read_text(encoding='utf-8');stem=Path(v['source']).stem
        md+=['',f"## {v['id']} — {v['name']}",'',v['caption'],'','```mermaid',source.strip(),'```']
        if v['id'] in eq:md+=['', '**Constraint:** '+eq[v['id']]]
        svg=ROOT/'assets/diagrams'/f'{stem}.svg'
        drawing=svg.read_text(encoding='utf-8') if svg.exists() else '<p>Rendered export pending; Mermaid source below is complete.</p>'
        pages.append('<section><h2>'+html.escape(v['id']+' — '+v['name'])+'</h2><p class="kind">'+html.escape(v['kind'])+'</p><p>'+html.escape(v['caption'])+'</p><div class="diagram">'+drawing+'</div>'+('<p class="equation">'+html.escape(eq[v['id']])+'</p>' if v['id'] in eq else '')+'<details><summary>Editable Mermaid source</summary><pre>'+html.escape(source)+'</pre></details></section>')
        checks.append(dict(id=v['id'],source=v['source'],source_sha256=hashlib.sha256(source.encode()).hexdigest(),element_references='PASS',rendered=svg.exists()))
    md+=['','## Notation and limits','','Composition diamonds appear in the block-style class diagrams. Requirement arrows labeled deriveReqt point to the parent need. Verify links express check intent. Undirected parametric lines denote equality bindings; they are not execution arrows. Diagram labels summarize the registry and tables, which retain detailed properties and typed interfaces.','', 'The activity-style decision view summarizes a batch comparison; it does not implement flight control. Read docs/architecture.md for allocations, mounting relationships and interface evidence.']
    (ROOT/'docs/diagram-book.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    css='body{font:16px/1.55 system-ui,sans-serif;color:#172b40;background:#f3f6fa;margin:0}main{max-width:1150px;margin:auto;padding:36px}header,section{background:white;padding:30px;margin-bottom:24px;border:1px solid #d8e1ec;border-radius:10px}h1,h2{line-height:1.2}h2{color:#123858}.kind{color:#456780;font-size:14px}.diagram{padding:16px 0;overflow:auto}.diagram svg{display:block;width:100%;max-height:850px;margin:auto}pre{white-space:pre-wrap;font-size:13px}.equation{background:#eef4f9;padding:14px}details{border-top:1px solid #d8e1ec;padding-top:12px}@media print{body{background:white}main{padding:0}section{break-before:page;border:0;padding:12px}details{display:none}.diagram svg{max-height:75vh}}'
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Relay mission envelope — diagram book</title><style>'+css+'</style><main><header><h1>Relay mission envelope</h1><p>Complete Mermaid architecture diagram book</p><p>'+html.escape(intro)+'</p><p>'+str(len(views))+' assembled views · source included · works offline</p></header>'+''.join(pages)+'</main></html>'
    (ROOT/'Diagram_Book.html').write_text(page,encoding='utf-8')
    (ROOT/'results/diagram-inventory.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    print(f'Assembled {len(views)} Mermaid views into Markdown and offline HTML')
if __name__=='__main__':build()
