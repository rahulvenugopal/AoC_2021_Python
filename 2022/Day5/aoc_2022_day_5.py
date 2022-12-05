# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:05:12 2022

@author: Rahul
"""
#%% --- Day 5: Supply Stacks --- Part 1

# Load data which is in text format
file = open('input','r')
data = file.readlines()

# Create 9 lists with entries being the strings
stack_of_crates = data[0:8]

list_of_crates = []

for stacks in range(9):
    temp_list_of_crates = []
    for rows in range(len(stack_of_crates)):
        if (stack_of_crates[rows][(stacks * 4)+1] != ' '):
            temp_list_of_crates.append(stack_of_crates[rows][(stacks * 4)+1])
    list_of_crates.append(list(reversed(temp_list_of_crates)))


# create another list with a three digit string for how many, from and to
instruction_for_crane = data[10::]

# removing all alphabets from string
import re
howmany_from_to = [(re.sub('[\D.]',' ', entries)).split() for entries in instruction_for_crane]

# Use remove and extend to move as per the crane
for runs, items in enumerate(howmany_from_to):
    add_back = []
    for pops in range(int(items[0])):
        add_back.append(list_of_crates[int(items[1])-1].pop())

    list_of_crates[int(items[2])-1].extend(add_back)

# get the last entries of the list_of_cranes
top_level_sequence = [entries[-1] for entries in list_of_crates]
''.join(top_level_sequence)


#%% --- Day 5: Supply Stacks --- Part 2

# cratemover 9001, BAMMMM

# Load data which is in text format
file = open('input','r')
data = file.readlines()

# Create 9 lists with entries being the strings
stack_of_crates = data[0:8]

list_of_crates = []

for stacks in range(9):
    temp_list_of_crates = []
    for rows in range(len(stack_of_crates)):
        if (stack_of_crates[rows][(stacks * 4)+1] != ' '):
            temp_list_of_crates.append(stack_of_crates[rows][(stacks * 4)+1])
    list_of_crates.append(list(reversed(temp_list_of_crates)))


# create another list with a three digit string for how many, from and to
instruction_for_crane = data[10::]

# removing all alphabets from string
import re
howmany_from_to = [(re.sub('[\D.]',' ', entries)).split() for entries in instruction_for_crane]

# Use remove and extend to move as per the crane
for runs, items in enumerate(howmany_from_to):
    add_back = []
    for pops in range(int(items[0])):
        add_back.append(list_of_crates[int(items[1])-1].pop())

        # reverse the add_back since 9001 model can retain position
        add_back = list(reversed(add_back))

    list_of_crates[int(items[2])-1].extend(add_back)

# get the last entries of the list_of_cranes
top_level_sequence = [entries[-1] for entries in list_of_crates]
''.join(top_level_sequence)

