# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:15:16 2022
AOC 2022
Day 1

@author: Rahul
"""
#%% --- Day 1: Calorie Counting --- Part 1

# Load data which is in text format
file = open('input','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# Create a list and keep adding the entries until we hit a break
# Once break comes append the sum and start afresh

# initialise a counter for elf's calories
elf_calories = []
sum = 0

for _, entries in enumerate(data):
    if entries != '':
        sum += int(entries)
    else:
        elf_calories.append(sum)
        sum = 0

# find the index of maximum calories
import numpy as np
which_elf = np.argmax(elf_calories)
print(str(which_elf) + 'th elf carry most calories')

calories_carried = elf_calories[which_elf]

#%% --- Day 1: Calorie Counting --- Part 2

last_three = np.sort(elf_calories)[[-1,-2,-3]]
last_three_sum = np.sum(last_three)
