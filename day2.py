# 12/17/2023
# https://adventofcode.com/2023/day/2

import sys
import re

prefix_re = re.compile("Game (\\d+)")
color_re = re.compile("(\\d+) (red|green|blue)")

class Game(object):
  index = None # int
  samples = None # {string: int}[]

  def __init__(self, line):
    self.line = line

    line_parts = line.split(":")
    prefix = line_parts[0]
    self.index = int(re.search(prefix_re, prefix).group(1))

    self.samples = []
    sample_parts = line_parts[1].split(";")
    for sample_part in sample_parts:
      sample = {}
      self.samples.append(sample)

      color_parts = sample_part.split(",")
      for color_part in color_parts:
        match = re.search(color_re, color_part)
        count = int(match.group(1))
        color = match.group(2)
        sample[color] = count

def sample_is_superset(a, b):
  for color, count in b.items():
    if color not in a or a[color] < count:
      return False
  return True

def colorwise_max(a, b):
  ret = {}
  all_colors = set(a.keys()).union(set(b.keys()))
  for color in all_colors:
    a_count = a[color] if color in a else 0
    b_count = b[color] if color in b else 0
    ret[color] = max(a_count, b_count)
  return ret

def sample_power(sample):
  total = 1
  for v in sample.values():
    total *= v
  return total

def part1(games):
  whole = {"red": 12, "green": 13, "blue": 14}

  total = 0
  for game in games:
    legal = True
    for sample in game.samples:
      if not sample_is_superset(whole, sample):
        legal = False
        break

    if legal:
      total += game.index

  return total

def part2(games):
  total = 0
  for game in games:
    accum = game.samples[0]
    for sample in game.samples:
      accum = colorwise_max(accum, sample)
    total += sample_power(accum)
  return total

def main():
  fname = sys.argv[1]

  games = []
  with open(fname, 'r') as f:
    for line in f:
      games.append(Game(line.strip()))

  print("Part 1: %s" % (part1(games),))
  print("Part 2: %s" % (part2(games),))

if __name__ == '__main__':
  main()
