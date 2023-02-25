import binpacking
from typing import List, Tuple

import json
import sys

input = json.loads(sys.stdin.read())

stor = input['storage']
typs = input['types']
top_slot = int(stor[-1]['slot'])
top_slot_size = int(typs[stor[-1]['type']]['numberOfBytes'])
slots_in_use = 1 + top_slot + (31 + top_slot_size) // 32
print(top_slot_size)

label_to_size = {}

for s in stor:
    id = s['label'] + "_" +  str(s['astId'])
    size = int(typs[s['type']]['numberOfBytes'])
    label_to_size[id] = size

bins = binpacking.pack(label_to_size, 32, num_to_beat=slots_in_use)
print(bins)
size_of_bins = 0
for b in bins:
    size_of_bins += (b.size + 31) // 32
if bins is None:
    print("No solution found that uses fewer than %d slots" % slots_in_use)
else:
    print("Storage is currently %d slots, can be reduced to %d slots or fewer" % (slots_in_use, size_of_bins))
    for b in bins:
        print(b)
