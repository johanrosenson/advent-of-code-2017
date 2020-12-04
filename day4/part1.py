# https://adventofcode.com/2017/day/4
import re

passphrases = open('input').read().splitlines()

valid = 0

for passphrase in passphrases:
    words = re.split(r'\s+', passphrase)
    unique_words = list(set(words))

    words.sort()
    unique_words.sort()

    if words == unique_words:
        valid += 1

print('Valid: {}'.format(valid))
