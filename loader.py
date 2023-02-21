from algos import parse_entry_points
class Contract:
    def __init__(self, path):
        self.path = path
    def read(self):
        with open(self.path, 'r') as file:
            return file.read()
    def entry_points(self):
        return parse_entry_points(self.read())

#tests
def tests():
    c = Contract('./main.rs')
    print(c.read())
    print(c.entry_points())
tests()
