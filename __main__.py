import binpacking
from typing import List, Tuple

import json
import sys

input = json.loads(sys.stdin.read())

stor = input['storage']
typs = input['types']

top_slot = int(stor[-1]['slot'])

label_to_size = {}

for s in stor:
    label_to_size[s['label']] = int(typs[s['type']]['numberOfBytes'])

bins = binpacking.pack(label_to_size, 32, num_to_beat=top_slot + 1)
print("Storage is currently %d slots, can be reduced to %d slots or fewer" % (top_slot + 1, len(bins)))
for b in bins:
    print(b)
