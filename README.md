# dna
A small python sequence analysis tool written in Python.

The program requires as its first command-line argument 
the name of a CSV file containing the STR (Short Tandem Repeats) counts for 
a list of individuals and should require as its second command-line argument 
the name of a text file containing the DNA sequence to identify.

Example: "$ python3 dna.py databases/large.csv sequences/5.txt"

If the program is executed with the incorrect number of command-line arguments, 
the program prints an error message.

The program opens the CSV file and reads its contents into memory.

The program opens the DNA sequence and reads its contents into memory.

If the STR counts match exactly with any of the individuals in the CSV file, the program prints out the name of the matching individual.
We assume that the STR counts will not match more than one individual.

If the STR counts do not match exactly with any of the individuals in the CSV file, the program prints "No match".




