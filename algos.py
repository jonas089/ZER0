import re

ERROR_LENGTH_MISMATCH = 0
def revert(error):
    print('Error code: ', error)
    return False

def parse_entry_points(c_string):
    entry_points = []
    oA = re.finditer('ENTRY_POINT', c_string)
    oE = re.finditer('END', c_string)
    oA_list = [occ for occ in oA]
    oE_list = [occ for occ in oE]
    if len(oA_list) != len(oE_list):
        revert(ERROR_LENGTH_MISMATCH)
    for i in range(0, len(oA_list)):
        _range = (oA_list[i].span(), oE_list[i].span())
        entry_points.append(c_string[int(_range[0][1])+1:int(_range[1][0])-1])
    return entry_points

def parse_entry_points_args(entry_points):
    meta = {
        'entry_points': [],
        'vec!': [],
        'ret': []
    }

    for i in range(0, len(entry_points)):
        nAE = re.finditer('NAME', entry_points[i])
        nAE_list = [ncc for ncc in nAE]
        _range = (nAE_list[0].span(), nAE_list[1].span())
        _name = entry_points[i][int(_range[0][1])+1:int(_range[1][0])-1]
        meta['entry_points'].append(_name)

        vAE = re.finditer('VEC', entry_points[i])
        vAE_list = [vcc for vcc in vAE]
        _range = (vAE_list[0].span(), vAE_list[1].span())
        _vec = entry_points[i][int(_range[0][1])+1:int(_range[1][0])-1]
        meta['vec!'].append(_vec)

        rAE = re.finditer('RET', entry_points[i])
        rAE_list = [rcc for rcc in rAE]
        _range = (rAE_list[0].span(), rAE_list[1].span())
        _res = entry_points[i][int(_range[0][1])+1:int(_range[1][0])-1]
        meta['ret'].append(_res)

    return meta
