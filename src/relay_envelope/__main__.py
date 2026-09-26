import argparse
from .report import run
p=argparse.ArgumentParser(description='Regenerate the illustrative relay comparison')
p.add_argument('--config',default='config/baseline.json');p.add_argument('--output',default='results')
a=p.parse_args();r=run(a.config,a.output);print('Provisional selection:',r['selected'])
