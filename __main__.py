from typing import List, Tuple

import json
import sys

input = json.loads(sys.stdin.read())

stor = input['storage']
typs = input['types']

topSlot = int(stor[-1]['slot'])
print("Used slots: %d" % (topSlot + 1))


label2sizeDict = {}

for s in stor:
    label2sizeDict[s['label']] = (int(typs[s['type']]['numberOfBytes']), s['type'])

label2size = [(x[0], x[1][0]) for x in label2sizeDict.items()]
label2size.sort(key=lambda x: x[1])

theoreticalLimit = (31 + sum([x[1] for x in label2size])) // 32

print("Theoretical slot limit: %d" % theoreticalLimit)

def ff_dec(l2s: List[Tuple[str, int]]):
    """Assumes list is sorted ascendingly, uses pop() to get elements from the end"""
    l2s = l2s.copy()
    labels = []
    bins = 0
    # Items larger than 32 bytes do not get packed.
    while len(l2s) > 0 and l2s[-1][1] >= 32:
        labels.append(l2s[-1][0])
        bins += (31 + l2s[-1][1]) // 32
        l2s.pop()
    while len(l2s) > 0:
        bins += 1
        rem = 32
        while len(l2s) > 0 and l2s[-1][1] <= rem:
            rem -= l2s[-1][1]
            labels.append(l2s[-1][0])
            l2s.pop()

    return (labels, bins)
            

(labels, bins) = ff_dec(label2size)
print("Storage is currently %d slots, can be reduced to %d slots or fewer" % (topSlot + 1, bins))
for l in labels:
    print(l, "(%s)" % label2sizeDict[l][1])
