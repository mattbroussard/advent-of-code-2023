# 12/18/2023
# https://adventofcode.com/2023/day/4

import sys
import re
from collections import defaultdict

prefix_re = re.compile("Card +(\\d+)")

class Card(object):
  winning = [] # int[]
  have = [] # int[]
  index = None # int

  def __init__(self, line):
    parts = line.split(":")
    self.index = int(re.search(prefix_re, parts[0]).group(1))

    parts = parts[1].split("|")
    self.winning = self.parse_int_list_str(parts[0])
    self.have = self.parse_int_list_str(parts[1])

  def parse_int_list_str(self, s):
    return [int(p) for p in s.split(" ") if len(p) > 0]

  def num_matches(self):
    win_set = set(self.winning)
    num_winning = 0
    for n in self.have:
      if n in win_set:
        num_winning += 1
    return num_winning

  def part1_score(self):
    num_winning = self.num_matches()
    if num_winning == 0:
      return 0

    return 2 ** (num_winning - 1)

def part1(cards):
  return sum(c.part1_score() for c in cards)

def part2(cards):
  have_counts = defaultdict(int)
  for i in range(len(cards)):
    assert cards[i].index == i + 1
    have_counts[i] += 1

  for i in range(len(cards)):
    num_matches = cards[i].num_matches()
    for j in range(num_matches):
      idx = i + j + 1
      if idx >= len(cards):
        continue
      have_counts[idx] += have_counts[i]

  return sum(have_counts.values())

def main():
  fname = sys.argv[1]

  cards = []
  with open(fname, 'r') as f:
    for line in f:
      cards.append(Card(line))

  print("Part 1: %s" % (part1(cards),))
  print("Part 2: %s" % (part2(cards),))

if __name__ == '__main__':
  main()
