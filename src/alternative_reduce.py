#!/usr/bin/env python3

import argparse
import glob
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
args = parser.parse_args()

paths = sorted(glob.glob('outputs/geoTwitter20-*.zip.lang'))

for hashtag in args.hashtags:
    counts = []

    for path in paths:
        with open(path) as f:
            data = json.load(f)

        counts.append(sum(data.get(hashtag, {}).values()))

    plt.plot(range(1, len(paths) + 1), counts, label=hashtag)

plt.xlabel('Day of Year')
plt.ylabel('Number of Tweets')
plt.legend()
plt.tight_layout()
plt.savefig('alternative_reduce.png')
