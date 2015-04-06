#!/usr/bin/env python

import sys

def main():
  codons = ['a','c','t','g']
  base = 0
  conversion = ""
  while base <= 33333333:
    conversion = str(base).zfill(8)
    index = 0
    while True:
      index = conversion.find('4')
      if index != -1:
        new = conversion.replace('4', '0')
        int_val = int(new[index - 1])

        conversion = new[index -1:].replace(str(int_val), str(int_val + 1), 1)
        conversion = new[:index -1] + conversion

        base = int(conversion)
      else:
        break
    codon_index = 0
    for codon in codons:
      conversion = conversion.replace(str(codon_index), codon)
      codon_index += 1
    base += 1
    print conversion

if __name__ == "__main__":
  main()