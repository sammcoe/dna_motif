# dna_motif
Python code that calculates the motif of large sets of DNA sequences using map reduce on hadoop

There are two different components:
  Mapper- Creates a key value pair output to feed to the reducer
  Reducer- Combines like output from mapper and computes the motif

This codes actually contains two versions of the program:

The first only calculates and outputs the overall motif and the total distance of it from the input sub-sequences.

The second also manages the individual given input sequences and their unique best matches against the end-calculated motif.
This code is currently commented out in the reducer, though the mapper still outputs the necessary information.  I have not been able to prove that this works exactly, as my attempts to run it have expended the hadoop cluster virtual machine memory on all attempts.  I know that it very nearly works, though I suspect some inefficiency that I am overlooking.

Running:
From the local filesystem containing the scripts, and with the input file on the hdfs, execut:

hadoop jar /usr/hdp/2.2.0.0-2041/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input [path to input on hdfs] -output [path to desired result directory]