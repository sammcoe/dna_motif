#!/usr/bin/env python
"Reducer script for calculating the motif of a given set of DNA"

from itertools import groupby
from operator import itemgetter
import sys

def get_map(file):
  for sequence in file:
    yield sequence.rstrip().split('\t', 1)

def get_metadata(group):
  for candidate, meta in group:
    yield meta.rstrip().split('\t', 1)

def main():
  # For testing locally: temp = open("map.txt")

  archive = []

  count = 0
  best_word = []
  best_count = 99999999999999999999
  best_match = ""
  score = 8
  index = 0
  input_index = 0
  dataset = get_map(sys.stdin)

  for current, group in groupby(dataset, itemgetter(0)):
    meta_list = get_metadata(group)
    for seq_num, info in groupby(meta_list, itemgetter(0)):
      for match, stats in info:
        info_list = stats.split('\t')
        count = count + int(info_list[2])
        if count < best_count:
          best_word = []
          best_word.append(current)
        elif count == best_count:
          best_word.append([current])
        info = list(info)
        info.append(current)
        archive.append(info)
    count = 0

  for motif in best_word:
    previous = 0
    for input_set in archive:
      if (input_set[-1] == motif):
        input_set.pop()
        best = 8
        for group in input_set:
          seq_data = group[1].split('\t')
          if int(seq_data[2]) < int(best):
            best = seq_data[2]
            best_match = seq_data[0]
            index = seq_data[1]
            input_index = group[0]
        #for best_word, best_match, score, index, input_index in index:
        print "Calculated Motif: %s.  Best matching sequence: %s had a distance of %s at index of %s in input sequence %s.  " % (motif, best_match, best, index, input_index)

if __name__ == "__main__":
  main()
