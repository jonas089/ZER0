import re
def parse_entry_points(string):
    e = []
    print('parsing entry points')
    oA = re.finditer('ENTRY_POINT', string)
    oE = re.finditer('END', string)
    oA_list = [occ for occ in oA]
    oE_list = [occ for occ in oE]
    for i in range(0, len(oA_list)):
        print(i)
    return e
