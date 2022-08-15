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

#%% creating lookup dictionary to tally scores
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

#%% Part Two

# laod data once more by running initial block of code

openers = ['(','[','{','<']

patterns_to_comb = ['()','[]','<>','{}']

# Find corrupted lines

corrupted_line_indices = []

# Loop line wise
for indices,lines in enumerate(data):

    # remove nested patterns recursively
    while any(substring in lines for substring in patterns_to_comb):
        for patterns in patterns_to_comb:
            lines = lines.replace(patterns, '')

    # remove opening strings
    for opening_strings in openers:
        lines = lines.replace(opening_strings,'')

    # pick up the first illegal character if line is corrupted
    if len(lines) >0:
        corrupted_line_indices.append(indices)

# Getting lines from data which are not corrupted
correct_indices = []

[correct_indices.append(indices) for indices, _ in enumerate(data) if indices not in corrupted_line_indices]

# subset the correct data
new_data = []

[new_data.append(lines) for location, lines in enumerate(data) if location in correct_indices]

#%%
import numpy as np
# replacing the opened braces with closing ones
look_up_dict_closer = {'(':')',
                '[':']',
                '{':'}',
                '<':'>'}

scoring_dict = {')':1,
                ']':2,
                '}':3,
                '>':4}

total_scores = []

for lines in new_data:
    # remove nested patterns recursively
    while any(substring in lines for substring in patterns_to_comb):
        for patterns in patterns_to_comb:
            lines = lines.replace(patterns, '')

    # fip the string to get the closing sequence
    lines = lines[::-1]

    data_lines = []

    for _,symbols in enumerate(lines):
        data_lines.append(look_up_dict_closer[symbols])

    for locs,entries in enumerate(data_lines):
        data_lines[locs] = scoring_dict[entries]

    auto_complete_scores = 0

    for scores in data_lines:
        auto_complete_scores = (auto_complete_scores*5) + scores

    total_scores.append(auto_complete_scores)

print(np.median(total_scores))