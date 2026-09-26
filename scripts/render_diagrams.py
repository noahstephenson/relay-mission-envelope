"""Render all assembled Mermaid views with mermaid-cli 12.0.0."""
import argparse,json,subprocess,tempfile,hashlib
from pathlib import Path
from build_diagram_book import build
ROOT=Path(__file__).resolve().parents[1]

def render(executable,puppeteer=None):
    views=json.loads((ROOT/'diagrams/index.json').read_text(encoding='utf-8'))
    out=ROOT/'assets/diagrams';out.mkdir(parents=True,exist_ok=True);records=[]
    with tempfile.TemporaryDirectory() as tmp:
        style=Path(tmp)/'mermaid-config.json'
        style.write_text(json.dumps({'theme':'neutral','flowchart':{'htmlLabels':False},'securityLevel':'strict'}),encoding='utf-8')
        for v in views:
            path=ROOT/v['source'];name=path.stem
            for ext in ('svg','png'):
                cmd=[executable,'-i',str(path),'-o',str(out/(name+'.'+ext)),'-c',str(style),'-b','white','--size','1400','-I',name]
                if puppeteer:cmd+=['-p',puppeteer]
                subprocess.run(cmd,check=True)
            records.append(dict(id=v['id'],name=name,source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),svg='assets/diagrams/'+name+'.svg',png='assets/diagrams/'+name+'.png',status='rendered; inspection recorded in verification report'))
    (ROOT/'results/diagram-rendering.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8');build()
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mmdc',default='mmdc');p.add_argument('--puppeteer-config');a=p.parse_args();render(a.mmdc,a.puppeteer_config)
