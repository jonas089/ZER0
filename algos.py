import re

ERROR_LENGTH_MISMATCH = 0
def revert(error):
    print('Error code: ', error)
    return False

def parse_entry_points(string):
    entry_points = []
    print('parsing entry points')
    oA = re.finditer('ENTRY_POINT', string)
    oE = re.finditer('END', string)
    oA_list = [occ for occ in oA]
    oE_list = [occ for occ in oE]
    if len(oA_list) != len(oE_list):
        revert(ERROR_LENGTH_MISMATCH)
    print(oA_list)
    print(oE_list)
    for i in range(0, len(oA_list)):
        _range = (oA_list[i].span(), oE_list[i].span())
        entry_points.append(string[int(_range[0][1])+1:int(_range[1][0])-1])
    return entry_points

def parse_entry_point_args(e_string):
    pass
