import json, os
from algos import parse_entry_points, parse_entry_points_args

class Contract:
    def __init__(self, path):
        self.path = path
        self.meta = None
    def read(self):
        with open(self.path, 'r') as file:
            return file.read()
    def entry_points(self):
        return parse_entry_points(self.read())
    def metadata(self):
        e = self.entry_points()
        e_list = []
        for ep in e:
            e_list.append(ep)
        contract_metadata = parse_entry_points_args(e_list)
        self.meta = contract_metadata
        return contract_metadata
    def dump_metadata(self):
        if self.meta == None:
            _meta = self.metadata()
        if os.path.exists('./meta.json'):
            os.remove('./meta.json')
        open('./meta.json', 'x')
        with open('./meta.json', 'w') as file:
            file.write(str(_meta))
#tests
def tests():
    c = Contract('./main.rs')
    c.dump_metadata()

tests()
