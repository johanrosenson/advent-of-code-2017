# https://adventofcode.com/2017/day/4
import re

passphrases = open('input').read().splitlines()

valid = 0

def contains_anagram(words):
    for n in range(len(words)-1):
        word = words[n]
        for anagram in words[n+1:]:
            sorted_word = ''.join(sorted(word))
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_word == sorted_anagram:
                return True
    return False;

for passphrase in passphrases:
    words = re.split(r'\s+', passphrase)
    unique_words = list(set(words))

    words.sort()
    unique_words.sort()

    if words != unique_words:
        continue

    # contains anagram
    if contains_anagram(words):
        continue

    valid += 1

print('Valid: {}'.format(valid))
