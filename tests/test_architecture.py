import unittest,copy,json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_architecture',ROOT/'scripts/build_architecture.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class ArchitectureTests(unittest.TestCase):
    def setUp(self):self.m=json.loads((ROOT/'model/architecture.json').read_text())
    def test_complete_registry(self):self.assertEqual(a.validate_model(self.m)['connectors'],12)
    def test_dangling_relation_rejected(self):
        self.m['relationships'][0]['target_id']='MISSING'
        with self.assertRaises(ValueError):a.validate_model(self.m)
    def test_wrong_port_direction_rejected(self):
        self.m['ports'][1]['is_conjugated']=False
        with self.assertRaises(ValueError):a.validate_model(self.m)
    def test_wrong_nested_occurrence_rejected(self):
        self.m['connectors'][5]['target_part_path']='AP3'
        with self.assertRaises(ValueError):a.validate_model(self.m)
    def test_wrong_binding_type_rejected(self):
        self.m['bindings'][0]['value_property_id']='CV02'
        with self.assertRaises(ValueError):a.validate_model(self.m)
    def test_requirement_verify_direction_rejected(self):
        rel=next(x for x in self.m['relationships'] if x['kind']=='verify')
        rel['source_id'],rel['target_id']=rel['target_id'],rel['source_id']
        with self.assertRaises(ValueError):a.validate_model(self.m)

if __name__=='__main__':unittest.main()
