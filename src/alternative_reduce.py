#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
args = parser.parse_args()

# imports
import glob
import json
import os
import matplotlib.pyplot as plt

# initialize data
data = {}

for hashtag in args.hashtags:
    data[hashtag] = []

# get all daily language files
paths = sorted(glob.glob('outputs/geoTwitter20-*.zip.lang'))

# scan through each day
for path in paths:

    with open(path) as f:
        counts = json.load(f)

    # get the date from the filename
    filename = os.path.basename(path)
    date = filename.replace('geoTwitter', '').replace('.zip.lang', '')

    # calculate total usage of each hashtag that day
    for hashtag in args.hashtags:

        if hashtag in counts:
            total = sum(counts[hashtag].values())
        else:
            total = 0

        data[hashtag].append(total)

# x-axis = day of year
days = range(1, len(paths) + 1)

# plot one line per hashtag
for hashtag in args.hashtags:
    plt.plot(days, data[hashtag], label=hashtag)

plt.xlabel('Day of Year')
plt.ylabel('Number of Tweets')
plt.title('Hashtag Usage During 2020')
plt.legend()
plt.tight_layout()

# save plot
plt.savefig('alternative_reduce.png')

print('saving alternative_reduce.png')
