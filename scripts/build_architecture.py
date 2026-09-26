"""Validate the neutral model registry and emit mapping/inspection tables.
These CSVs are readable architecture and traceability tables.
"""
import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def resolve(value,path):
    for key in path.split('.'):
        value=value[int(key)] if isinstance(value,list) else value[key]
    return value

def validate_model(m):
    groups=['packages','elements','relationships','parts','value_properties','ports','connectors','bindings','diagrams']
    all_ids=[v['id'] for g in groups for v in m[g]]
    if len(all_ids)!=len(set(all_ids)): raise ValueError('Duplicate global model ID')
    packages={v['id']:v for v in m['packages']};elements={v['id']:v for v in m['elements']}
    parts={v['id']:v for v in m['parts']};ports={v['id']:v for v in m['ports']}
    props={v['id']:v for v in m['value_properties']};constraints={v['id']:v for v in m['constraints']}
    known=set(packages)|set(elements)
    def require(id,ids):
        if id not in ids: raise ValueError('Unresolved model reference: '+id)
    for p in packages.values():
        if p['parent_id']:require(p['parent_id'],packages)
        visited={p['id']};parent=p['parent_id']
        while parent:
            if parent in visited:raise ValueError('Package containment cycle')
            visited.add(parent);parent=packages[parent]['parent_id']
    for e in elements.values():require(e['package_id'],packages)
    for rel in m['relationships']:
        require(rel['source_id'],elements);require(rel['target_id'],elements)
        s=elements[rel['source_id']];t=elements[rel['target_id']]
        if rel['kind']=='deriveReqt' and (s['kind']!='Requirement' or t['kind']!='Requirement'):raise ValueError('Requirement derivation endpoint type')
        if rel['kind']=='verify' and (s['kind']!='TestCase' or t['kind']!='Requirement'):raise ValueError('Verify direction/type')
    for p in parts.values():
        require(p['owner_id'],elements);require(p['type_id'],elements)
        if elements[p['type_id']]['kind']!='Block':raise ValueError('Part type must be Block')
    for p in props.values():
        require(p['owner_id'],elements);require(p['type_id'],elements)
        if elements[p['type_id']]['kind']!='ValueType':raise ValueError('Value property type')
    for p in ports.values():
        require(p['owner_id'],elements);require(p['type_id'],elements)
        if elements[p['type_id']]['kind']!='InterfaceBlock':raise ValueError('Proxy port type')
    def path_owner(owner,path):
        for pid in path.split('/'):
            require(pid,parts);p=parts[pid]
            if p['owner_id']!=owner:raise ValueError('Invalid nested part path: '+path)
            owner=p['type_id']
        return owner
    for c in m['connectors']:
        require(c['owner_id'],elements)
        for side in ('source','target'):
            require(c[side+'_port_id'],ports);p=ports[c[side+'_port_id']]
            if path_owner(c['owner_id'],c[side+'_part_path'])!=p['owner_id']:raise ValueError('Port owner does not match part occurrence')
            if p['type_id']!=c['interface_id']:raise ValueError('Connector interface mismatch')
        s=ports[c['source_port_id']];t=ports[c['target_port_id']]
        if elements[c['interface_id']]['flow_properties'] and s['is_conjugated']==t['is_conjugated']:raise ValueError('Same effective flow direction at both ends')
    for c in constraints.values():
        require(c['id'],elements)
        for p in c['parameters']:require(p['type_id'],elements)
    for b in m['bindings']:
        require(b['constraint_type_id'],constraints);require(b['value_property_id'],props)
        p=props[b['value_property_id']];params={p['name']:p for p in constraints[b['constraint_type_id']]['parameters']}
        if b['parameter'] not in params or params[b['parameter']]['type_id']!=p['type_id']:raise ValueError('Binding type mismatch')
        if p['owner_id']!=b['owner_id']:raise ValueError('Binding outside value context')
    for d in m['diagrams']:
        require(d['owner_id'],known)
        for id in d['element_ids']:require(id,elements)
    for i in range(1,9):
        if not any(x['kind']=='verify' and x['target_id']==f'R{i}' for x in m['relationships']):raise ValueError('Missing verification intent')
    for i in range(1,7):
        if not any(x['kind']=='allocate' and x['source_id']==f'F{i}' for x in m['relationships']):raise ValueError('Unallocated function')
    return {g:len(m[g]) for g in groups}

def export_csv(path,rows):
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for row in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})

def build():
    m=json.loads((ROOT/'model/architecture.json').read_text(encoding='utf-8'));counts=validate_model(m)
    c=json.loads((ROOT/'config/baseline.json').read_text(encoding='utf-8'));result=json.loads((ROOT/'results/baseline.json').read_text(encoding='utf-8'))
    expected=hashlib.sha256(json.dumps(c,sort_keys=True).encode()).hexdigest()
    if result['input_sha256']!=expected: raise ValueError('Stale baseline results: regenerate before exporting slots')
    out=ROOT/'model/tables';out.mkdir(exist_ok=True)
    for key in ['packages','elements','relationships','parts','value_properties','ports','connectors','constraints','bindings','diagrams']:export_csv(out/(key+'.csv'),m[key])
    export_csv(out/'requirements.csv',[{k:e.get(k,'') for k in ['id','name','requirement_text','package_id','evidence_status','config_path']} for e in m['elements'] if e['kind']=='Requirement'])
    slots=[]
    for option in result['options']:
        bid,sid=option['option_id'].split('-');battery=next(b for b in c['batteries'] if b['id']==bid)
        for p in m['value_properties']:
            source=p['source']
            value=resolve(c,p['path']) if source=='config' else resolve(battery,p['path']) if source=='battery' else resolve(option,p['path']) if source=='result' else next(x['bus_power_w'] for x in option['ledger'] if x['segment']=='relay')
            slots.append(dict(case_id=option['option_id'],property_id=p['id'],owner_type_id=p['owner_id'],property_name=p['name'],type_id=p['type_id'],value=value,source=source,source_path=p['path'],status='illustrative input' if source in ['config','battery'] else 'calculated under assumptions'))
    export_csv(out/'configuration-slots.csv',slots)
    md=['# Model catalog','','Generated from `model/architecture.json`; edit the JSON and rebuild. The complete visual architecture is assembled in docs/diagram-book.md.','', '| ID | Name | Type | Package |','|---|---|---|---|']
    md += [f"| {e['id']} | {e['name']} | {e['kind']} | {e['package_id']} |" for e in m['elements']]
    md += ['', '## Diagram inventory','', '| ID | View | Owner | Purpose |','|---|---|---|---|']
    md += [f"| {d['id']} | {d['name']} | {d['owner_id']} | {d['purpose']} |" for d in m['diagrams']]
    (ROOT/'model/CATALOG.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    report={'status':'PASS','scope':'registry references, allocations, typed ports and bindings; not physical validation or formal SysML conformance','counts':counts,'configuration_slots':len(slots),'architecture_sha256':hashlib.sha256((ROOT/'model/architecture.json').read_bytes()).hexdigest()}
    (ROOT/'results/model-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':build()
