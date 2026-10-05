#!/bin/bash

for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    nohup python map.py "$file" > "outputs/$(basename "$file").lang" 2>&1 &
done
