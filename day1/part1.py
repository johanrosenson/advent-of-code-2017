# https://adventofcode.com/2017/day/1

digits = open('input').read()

digits_sum = 0

length = len(digits)
offset = 1

for i in range(length):
    digit = digits[i]
    next_digit = digits[(i+offset) % length]

    if digit == next_digit:
        digits_sum += int(digit)

print('Matches: {}'.format(digits_sum))
