# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:38:45 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 10: Syntax Scoring ---Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# creating lookup dictionary to tally scores
look_up_dict = {')':3,
                ']':57,
                '}':1197,
                '>':25137}

openers = ['(','[','{','<']

patterns_to_comb = ['()','[]','<>','{}']

# Find consecutive occurences of opposing brackets and delete them
# keep doing that until none remains
# count the unique symbols

# initialise illegal character list
illegal_list = []

# Loop line wise
for lines in data:

    # remove nested patterns recursively
    while any(substring in lines for substring in patterns_to_comb):
        for patterns in patterns_to_comb:
            lines = lines.replace(patterns, '')

    # remove opening strings
    for opening_strings in openers:
        lines = lines.replace(opening_strings,'')

    # pick up the first illegal character if line is corrupted
    if len(lines) >0:
        illegal_list.append(lines[0])

# replace the illegal charcter by looking up the dictionary
scores = 0
for illegals in illegal_list:
    scores += look_up_dict[illegals]

print(scores)


