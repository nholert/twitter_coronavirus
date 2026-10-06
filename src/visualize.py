#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort from high to low and keep only the top 10
items = sorted(
    counts[args.key].items(),
    key=lambda item: (item[1], item[0]),
    reverse=True
)[:10]

# sort those top 10 from low to high for the graph
items = sorted(items, key=lambda item: item[1])

keys = [k for k, v in items]
values = [v for k, v in items]

# make bar graph
plt.bar(keys, values)

plt.xlabel('Key')
plt.ylabel('Value')
plt.title(args.key)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# create output filename
output_path = os.path.basename(args.input_path) + '.' + args.key.replace('#', '') + '.png'

plt.savefig(output_path)
print('saving', output_path)
