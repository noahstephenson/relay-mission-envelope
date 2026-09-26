"""One command to rebuild calculations, tests, handoff tables and evidence."""
import os,sys,subprocess,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(args,save=None):
    env=dict(os.environ);env['PYTHONPATH']=str(ROOT/'src')+os.pathsep+env.get('PYTHONPATH','')
    result=subprocess.run([sys.executable,*args],cwd=ROOT,env=env,text=True,capture_output=True)
    if save:(ROOT/save).write_text(result.stdout+result.stderr,encoding='utf-8')
    print(' '.join(args));print(result.stdout+result.stderr,end='')
    if result.returncode:raise SystemExit(result.returncode)

if __name__=='__main__':
    (ROOT/'results').mkdir(exist_ok=True)
    run(['-m','unittest','discover','-s','tests','-v'],'results/test-report.txt')
    run(['-m','relay_envelope'])
    run(['physics/analytical_starter.py'],'results/algebra-checks.json')
    run(['scripts/build_evidence.py'])
    run(['scripts/build_gap_review.py'])
    run(['scripts/run_acceptance_cases.py'])
    run(['scripts/build_architecture.py'])
    run(['scripts/build_diagram_book.py'])
    print('Complete. Included Mermaid exports can be refreshed with scripts/render_diagrams.py.')
