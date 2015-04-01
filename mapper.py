#!/usr/bin/python

# Mapper script for calculating the motif of a given set of DNA
#
# Author: Samuel Coe
# Website: samuelm.co

import sys

MOTIF_LEN = 8

def get_sequences(data, length):
  start = 0
  # Increment through entire file, through every
  # possible sequence.
  # If the first line is 'tacatgact', then first pass is
  # 'tacatgac' and the second pass is 'acatgact'
  for char in data:
    if len(data) >= (start + MOTIF_LEN):
      yield data[start:length]
      start += 1
      length += 1

def sequence_perm():
  # This function produces a purmutation of all ~40k
  # codon combinations for a sequence of 8 bytes
  # composed of a, c, t, g, and u
  codons = ['a','c','t','g','u']

  # The function treats the DNA sequences as a number
  # and uses a map to substitute the corresponding letters
  # Start count at 0
  base = 0
  conversion = ""

  # Since there are 5 DNA codons, we need to count up
  # to 8 digits of 4 (count is zero inclusive), so each
  # byte has 5 states.
  while base < 44444444:
    base += 1
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
      index = conversion.find('5')
      if index != -1:
        # Replace 5 with 0
        new = conversion.replace('5', '0')
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
    print conversion

def main():
  # Get sequences from file
  data_set = open('promoters_data_clean.txt')
  data = data_set.read()
  clean_data = data.replace("\r", "")
  data = clean_data.replace("\n", "")

  # This will be used to determine when all sequences have been read
  sequences = get_sequences(data, MOTIF_LEN)

  # Write the DNA words to stdout to be picked up my
  # hadoop streaming
  for sequence in sequences:
#    print '%s\t%d' % (sequence, 1)

if __name__ == "__main__":
  main()
