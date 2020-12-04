# https://adventofcode.com/2017/day/2
import re

rows = open('input').read().splitlines()

checksum = 0

for row in rows:
    cells = [int(v) for v in filter(None, re.split(r'\s+', row))]
    for i in range(len(cells)-1):
        n = cells[i]
        for j in cells[i+1:]:
            if max(n, j) % min(n, j) == 0:
                checksum += int(max(n, j) / min(n, j))

print('checksum: {}'.format(checksum))
