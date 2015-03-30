#!/usr/bin/env python
"Reducer script for calculating the motif of a given set of DNA"

from itertools import groupby
from operator import itemgetter
import sys

def get_map(file):
  for sequence in file:
    yield sequence.rstrip().split('\t', 1)

def main():
 # temp = open("temp.txt")
  motif = get_map(sys.stdin)
  for current, group in groupby(motif, itemgetter(0)):
    try:
      best_word = sum(int(count) for current, count in group)
      print "%s" % (best_word)
    except ValueError:
      pass

if __name__ == "__main__":
  main()
