# 12/17/2023
# https://adventofcode.com/2023/day/3

import sys
import re
from collections import defaultdict

def coords_of_word(word, word_origin):
  xo, y = word_origin
  for i in range(len(word)):
    yield (xo + i, y)

def neighbors(point):
  x, y = point
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0:
        continue
      yield (x + dx, y + dy)

def neighbors_of_word(word, word_origin):
  visited = set()
  for c in coords_of_word(word, word_origin):
    for n in neighbors(c):
      if n in visited:
        continue
      visited.add(n)
      yield n

def is_symbol(c):
  return c is not None and c != "." and c not in "0123456789"

class Grid(object):
  def __init__(self, lines):
    self.lines = lines

  def get_numbers(self):
    r = re.compile("\\d+")
    for y, line in enumerate(self.lines):
      for match in re.finditer(r, line):
        num = match.group(0)
        x = match.start()
        yield (num, (x, y))

  def __getitem__(self, key):
    x, y = key
    if y < 0 or y >= len(self.lines):
      return None
    if x < 0 or x >= len(self.lines[y]):
      return None
    return self.lines[y][x]

def part1(grid):
  total = 0

  for num, pos in grid.get_numbers():
    any_symbol = False
    for n in neighbors_of_word(num, pos):
      if is_symbol(grid[n]):
        any_symbol = True
        break

    if any_symbol:
      total += int(num)

  return total

def part2(grid):
  total = 0

  gears = defaultdict(list)
  for num, pos in grid.get_numbers():
    for n in neighbors_of_word(num, pos):
      if grid[n] == "*":
        gears[n].append(int(num))

  for part_nums in gears.values():
    if len(part_nums) != 2:
      continue

    ratio = part_nums[0] * part_nums[1]
    total += ratio

  return total

def main():
  fname = sys.argv[1]

  with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    grid = Grid(lines)

  print("Part 1: %s" % (part1(grid),))
  print("Part 2: %s" % (part2(grid),))

if __name__ == '__main__':
  main()
