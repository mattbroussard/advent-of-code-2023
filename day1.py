# 12/17/2023
# https://adventofcode.com/2023/day/1

import sys
import re

def part1(lines):
  total = 0
  for line in lines:
    digits = [c for c in line if c in "0123456789"]

    # debug; should never happen in valid input if impl is correct
    # sample input for part 2 is invalid for part 1, though
    if len(digits) < 1:
      # print("insufficient digits; line=\"%s\", digits=%s" % (line, digits))
      digits = ["0"]

    val = int(digits[0] + digits[-1])
    total += val

  return total

# reverse option is to deal with overlapping matches at end of string, which should be greedy from the right
def part2_transform(line, reverse=False):
  names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  if reverse:
    names = [s[::-1] for s in names]
    line = line[::-1]
  r = re.compile("|".join(names))

  # manually implement replace all since the sample input specifies that for overlapping matches
  # we should match greedily; e.g. eightwo should match 8 before 2
  while True:
    match = re.search(r, line)
    if not match:
      break

    val = names.index(match.group(0)) + 1
    line = line[:match.start()] + str(val) + line[match.end():]

  if reverse:
    line = line[::-1]

  return line

def part2(lines):
  return part1(
    # since it's theoretically possible end and beginning matches to overlap, we concat both
    # transformed versions (looking from left or right) so they show up separately to part1 function.
    # Since we only care about first/last digits, repeating stuff in the middle doesn't matter.
    part2_transform(line) + part2_transform(line, reverse=True)
    for line in lines
  )

def main():
  fname = sys.argv[1]

  with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

  print("Part 1: %s" % (part1(lines),))
  print("Part 2: %s" % (part2(lines),))

if __name__ == '__main__':
  main()
