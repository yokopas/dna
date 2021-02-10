from sys import argv
import csv

# secure correct command
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequense.txt")
    exit(1)

# open csv file
with open(argv[1],'r') as csvfile:
    reader = csv.DictReader(csvfile)    
    
    # extract patterns_list list to search them for in a dna sequence
    for row in reader:
        patterns_list = list(row.keys())
        break

# open txt file wit a dna sequence       
sequence_hand = open(argv[2])
for line in sequence_hand:
    sequence = line

# make dict with patterns_list as keys and max number of repated occurrence in the sequence as values
occurrence  = {}
for pattern in patterns_list:
    l = len(pattern)
    tmax = 0
    temp = 1
    for i in range(l,len(sequence)):
        if sequence[i-l:i] == pattern and sequence[i-l-l:i-l] == pattern:
            temp += 1
            if temp > tmax:
                tmax = temp
        if sequence[i-l:i] == pattern and sequence[i-l-l:i-l] != pattern:
            temp = 1
    occurrence[pattern] = str(tmax)   
        
# make a list from dna sequence to compare 
pattern_count = list(occurrence.values())

# compare sequence list with csv file data
with open(argv[1],'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_list = list(row.values())
        if csv_list[1:] == pattern_count[1:]:
            print(csv_list[0])
            quit()
print("No match")
        






