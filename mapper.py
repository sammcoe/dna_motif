#!/usr/bin/env python

# Mapper script for calculating the motif of a given set of DNA
#
# Author: Samuel Coe
# Website: samuelm.co

import sys

def get_sequences(file, l):
  # Get the total length of the file
  # This will be used to determine when all sequences have been read
  chars = (len(file) - l)
  start = 0
  end = 7
  # Increment through entire file, through every
  # possible sequence.
  # If the first line is 'tacatgact', then first pass is
  # 'tacatgac' and the second pass is 'acatgact'
  for chars in file:
    yield file[start:end]
    start += 1
    end += 1

