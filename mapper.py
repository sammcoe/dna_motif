#!/usr/bin/python

# Mapper script for calculating the motif of a given set of DNA
#
# Author: Samuel Coe
# Website: samuelm.co

import sys
from array import array

MOTIF_LEN = 8

def get_sequences(data, length):
  start = 0
  clean_data = data.replace('\n', '').replace('\r', '')

  # Increment through entire file, through every
  # possible sequence.
  # If the first line is 'tacatgact', then first pass is
  # 'tacatgac' and the second pass is 'acatgact'
  for char in clean_data:
    if len(clean_data) >= (start + MOTIF_LEN):
      yield '%s\t%i' % (clean_data[start:length], start)
      start += 1
      length += 1

def sequence_perm():
  # This function produces a purmutation of all ~40k
  # codon combinations for a sequence of 8 bytes
  # composed of a, c, t, g, and u
  codons = ['a','c','t','g']

  # The function treats the DNA sequences as a number
  # and uses a map to substitute the corresponding letters
  # Start count at 0
  base = 0
  conversion = ""

  # Since there are 5 DNA codons, we need to count up
  # to 8 digits of 4 (count is zero inclusive), so each
  # byte has 5 states.
  # For prod: 
  while base <= 33333333:
  # For testing locally: while base <= 00000100:
    # Pad the base number to get a string sequence
    conversion = str(base).zfill(8)
    index = 0
    # Since there are only 5 codons, if any number
    # within the sequence reaches 5, it is beyond the
    # index limit of 0 to 4. Replace it with zero and
    # increment the next highest order bit.
    # This sequence repeats until no bytes are bumped
    # up to 5.
    while True:
      index = conversion.find('4')
      if index != -1:
        # Replace 5 with 0
        new = conversion.replace('4', '0')
        # Find the standing value of the bit that is
        # one order higher than the bit being set back to zero
        int_val = int(new[index - 1])
        # Replace the higher order bit with its current value plus 1
        conversion = new[index -1:].replace(str(int_val), str(int_val + 1), 1)
        conversion = new[:index -1] + conversion
        # Get the new integer base value to increment
        base = int(conversion)
      else:
        break
    # Set a counter variable to correspond to the incrementing
    # index of the replacement codon array
    codon_index = 0
    # Replace numerical values with corresponding alphanumeric value
    for codon in codons:
      conversion = conversion.replace(str(codon_index), codon)
      codon_index += 1
    base += 1
    yield conversion

def main():
  best_dist = 8
  median_word = ""
  best_match = ""
  index = ""
  data = ""
  seq_val = 0

  # Get the stdin for input sequences
  dna_file = sys.stdin

  # Get permutation of sequences for possible candidates
  candidates = sequence_perm()

  # This will be used to determine when all lines have been read
  for lines in dna_file:
    # Value to maintain the input sequence number
    seq_val = seq_val + 1
    # For each in the permutation of possible sequences
    for candidate in candidates:
      # Get the sub-sequences for the current input sequence
      sequences = get_sequences(lines, MOTIF_LEN)
      # For each sub-sequence in the current input sequence
      for sequence in sequences:
        # Split the sub-sequence from the index of the sub-sequence
        current = sequence.split('\t')
        # Get the current sub-sequence
        current_seq = current[0]
        # Calculate the distance between the current candidate and the current sub-sequence
        dist = distance(current_seq, candidate)
        # Print the result to stdout for the reducer, candidate will be the key
        print '%s\t%i\t%s\t%d' % (candidate, seq_val, sequence, dist)


# Simple function to calculate distance between two words
def distance(seq1, seq2):
  # First, check if the sequences match
  if seq1 == seq2:
    return 0
  
  # Check for the obvious scenarious of totally
  # oposite lengths
  len1, len2 = len(seq1), len(seq2)
  if len1 == 0:
    return len2
  if len2 == 0:
    return len1
  if len1 < len2:
    len1, len2 = len2, len1
    seq1, seq2 = seq2, seq1
  
  column = array('L', range(len2 + 1))

  # Calculate the distance by comparing each byte
  for x in range(1, len1 + 1):
    column[0] = x
    last = x - 1
    for y in range(1, len2 + 1):
      old = column[y]
      cost = int(seq1[x - 1] != seq2[y - 1])
      column[y] = min(column[y] + 1, column[y - 1] + 1, last + cost)
      last = old
  
  return column[len2]

if __name__ == "__main__":
  main()
