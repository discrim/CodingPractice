def deleteBetween(whole, start, end):
    idx1 = whole.find(start) + len(start)
    idx2 = whole.find(end)
    assert idx1 != -1, "%s does not exist" % start
    assert idx2 != -1, "%s does not exist" % end
    print(idx1, idx2)
    print(whole[idx1 - 3:idx1 + 4])
    print(whole[idx2 - 3:idx2 + 4])
    return whole[:idx1] + whole[idx2:]


def deleteCertain(whole, target):
    idx = whole.find(target)
    assert idx != -1, "%s does not exist" % target
    print(idx)
    if idx + len(target) < len(whole):
        return whole[:idx] + whole[idx + len(target):]
    else:
        return whole[:idx]


def main1():
    aa = "abcdefghij"
    ######0123456789
    print(aa)
    bb = deleteBetween(aa, "cd", "hi")
    print(bb)


def main2():
    #aa = "\xfcd\x01(\xfdd\x01\xda\xb0\xb1vP\x01".encode('unicode_escape')
    aa = b'5b:f8"}\xfcd\x01(\xfdd\x01\xda\xb0\xb1vP\x01, "anten'
    print(aa)
    bb = deleteBetween(aa, b"\"}", b", ")
    print(bb)

import json
from prettyjson import prettyjson
def main3():
    aa = b'{"I":[ [0,-0.236], [1,0.370], [2,0.079], [3,-0.339], [4,-0.079], [5,-0.142], [6,0.118], [7,0.016], [8,0.000], [9,-0.472], [10,0.220], [11,0.102], [12,0.181], [13,0.055], [14,0.087], [15,0.260], ], "Q":[ [0,-0.205], [1,-0.055], [2,0.315], [3,-0.591], [4,-0.307], [5,0.157], [6,0.339], [7,-0.717], [8,-0.520], [9,-0.008], [10,0.559], [11,-0.969], [12,-0.134], [13,-0.031], [14,0.504], [15,-0.598], ], "MAC": "08:6b:d7:36:5b:f8", "timestamp": 1594224221.360880, "request": { "request_type": "locate_asset", "MAC": "08:6b:d7:36:5b:f8"}\xfcd\x01(\xfdd\x01\xda\xb0\xb1vP\x01, "antenna": {}}\x00'
    bb = deleteBetween(aa, b'\"}', b', "ant')
    print("bb: ", bb)
    cc = deleteCertain(bb, b'\x00')
    print("cc: ", cc)
    
    dd = cc.decode()
    print("type(dd): ", type(dd))
    print("dd: ", dd)

    
    ee = prettyjson(dd)
    print("ee: \n", ee)


if __name__ == '__main__':
    main3()