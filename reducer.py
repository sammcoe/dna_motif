#!/usr/bin/env python

# Reducer script for calculating the motif of a given set of DNA
#
# Author: Samuel Coe
# Website: samuelm.co

from itertools import groupby
from operator import itemgetter
import sys

# Get the output from the mapper
def get_map(file):
  for sequence in file:
    yield sequence.rstrip().split('\t', 1)

# Get the metadata sent along with the mapper output
def get_metadata(group):
  for candidate, meta in group:
    yield meta.rstrip().split('\t', 1)

def main():
  # An archive of all comparisons, used for picking out
  # the best match of each input sequences after the motif
  # has been calculated
  archive = []

  count = 0
  best_word = ""
  best_count = 99999999999999999999
  best_match = ""
  score = 8
  index = 0
  input_index = 0
  # Get the output of mapper from stdin
  dataset = get_map(sys.stdin)

  print "Motif\t\tDistance"

  # Only calculates the motif and the total distance for all
  # sub-sequences from the motif.

  # For the current motif candidate and its relevant info
  # in each input sequence grouped by motif candidates
  for current, group in groupby(dataset, itemgetter(0)):
    # For the given meta data included with each candidate
    for data in group:
      # Split the meta data into a list
      data_list = data[1].rstrip().split('\t')
      # Add the distances for each group
      count = count + int(data_list[3])
    # If the count for each group is less than the current best
    # assign current count to best, and current candidate as the motif
    if count < best_count:
      best_count = count
      best_word = data[0]
    # Reset count for each candidate
    count = 0

    print "%s\t%s" % (best_word, best_count)

  # This is for the more complicated version of the calculation.
  # It stores all relevant info and outputs the best match to the motif
  # from every input sequence.  I'm having difficulty testing and proving it
  # works because the hadoop system run out of physical memory, but it should
  # work, or almost work.
'''
  for current, group in groupby(dataset, itemgetter(0)):
    meta_list = get_metadata(group)
    for seq_num, info in groupby(meta_list, itemgetter(0)):
      for match, stats in info:
        info_list = stats.split('\t')
        count = count + int(info_list[2])
        if count < best_count:
          best_word = current
        info = list(info)
        info.append(current)
        archive.append(info)
    count = 0

  print "Motif\t\tMatch\t\tDistance\tIndex\tInSeq"

  for input_set in archive:
    if (input_set[-1] == best_word):
      input_set.pop()
      best = 8
      for group in input_set:
        seq_data = group[1].split('\t')
        if int(seq_data[2]) < int(best):
          best = seq_data[2]
          best_match = seq_data[0]
          index = seq_data[1]
          input_index = group[0]
      print "%s\t%s\t%s\t\t%s\t%s" % (best_word, best_match, best, index, input_index)
    else:
      archive.remove(input_set)
'''
if __name__ == "__main__":
  main()
