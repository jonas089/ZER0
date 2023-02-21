from loader import Contract

def test():
    # load contract
    c = Contract('./inputs/main.rs')
    # create json artifact
    c.dump_metadata()
    # restore original contract
    c.sanitize()
test()
