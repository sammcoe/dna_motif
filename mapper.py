#!/usr/bin/env python

# Mapper script for calculating the motif of a given set of DNA
#
# Author: Samuel Coe
# Website: samuelm.co

import sys

def get_sequences(file, length):
  # Get the total length of the file
  # This will be used to determine when all sequences have been read
  data = file.read()
  start = 0
  # Increment through entire file, through every
  # possible sequence.
  # If the first line is 'tacatgact', then first pass is
  # 'tacatgac' and the second pass is 'acatgact'
  for char in data:
    yield data[start:length]
    start += 1
    length += 1

def main():
  # Get sequences from file
  data_set = open('promoters_data_clean.txt')
  sequences = get_sequences(data_set, 8)

  for sequence in sequences:
    print '%s\t%d' % (sequence, 1)

if __name__ == "__main__":
  main()