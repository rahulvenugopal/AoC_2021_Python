# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:11:26 2022
AOC 2022
@author: Rahul
"""
#%% --- Day 4: Camp Cleanup --- Part 1

# Load data which is in text format
file = open('input','r')
data = file.readlines()
data = [line.rstrip() for line in data]


# Run a loop for entries and for each entry split by ,

counter = 0

for entries in data:
    elf_one, elf_two = entries.split(',')

    # get the start and end ID series to clean
    elf_one_cleaned = set(list(range(int(elf_one.split('-')[0]),
                            int(elf_one.split('-')[1])+1)))

    elf_two_cleaned = set(list(range(int(elf_two.split('-')[0]),
                            int(elf_two.split('-')[1])+1)))

    # cehck if either is a subset of other
    if elf_one_cleaned.issubset(elf_two_cleaned) or elf_two_cleaned.issubset(elf_one_cleaned):
        counter += 1

print(counter)

#%% --- Day 4: Camp Cleanup --- Part 2

counter = 0

for entries in data:
    elf_one, elf_two = entries.split(',')

    # get the start and end ID series to clean
    elf_one_cleaned = set(list(range(int(elf_one.split('-')[0]),
                            int(elf_one.split('-')[1])+1)))

    elf_two_cleaned = set(list(range(int(elf_two.split('-')[0]),
                            int(elf_two.split('-')[1])+1)))

    # cehck if either is a subset of other
    if bool(elf_one_cleaned & elf_two_cleaned):
        counter += 1

print(counter)