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
  best_word = ""
  best_count = 0
  dataset = get_map(sys.stdin)
  for current, group in groupby(dataset, itemgetter(0)):
    try:
      tally = sum(int(count) for current, count in group)
      print "%s\t%s" % (tally, current)
      if tally > best_count:
        best_word = current
        best_count = tally
    except ValueError:
      pass
  print "Calculated Motif: %s.  Occurred %i times." % (best_word, best_count)

if __name__ == "__main__":
  main()
agtcu