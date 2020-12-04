# https://adventofcode.com/2017/day/2
import re

rows = open('input').read().splitlines()

checksum = 0

for row in rows:
    cells = [int(v) for v in filter(None, re.split(r'\s+', row))]
    checksum += max(cells) - min(cells)

print('checksum: {}'.format(checksum))
