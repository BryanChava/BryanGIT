# BRYAN CHAVARRIA
# 1657040

import csv

fileName = input()

wordsFrequency = {}


with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
            else:
                wordsFrequency[word] += 1
for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key]))
