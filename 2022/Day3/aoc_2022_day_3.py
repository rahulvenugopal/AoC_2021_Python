# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:01:18 2022
AOC 2022
Day 2
@author: Rahul
"""
#%% --- Day 3: Rucksack Reorganization --- Part 1

# Load data which is in text format
file = open('input','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# initialise the common component
common_item = []

# Load each item of list, split it into half and find the common element
for _,entries in enumerate(data):
    first_compartment = entries[0:int(len(entries)/2)]
    second_compartment = entries[int(len(entries)/2):]
    
    # find the intersection to get the common item
    common = set(first_compartment).intersection(second_compartment).pop()
    
    common_item.append(common)
    
# creating mapping
import string

mapping_lists = []
values = []

for i in string.ascii_lowercase:
    mapping_lists.append(i)

for i in string.ascii_uppercase:
    mapping_lists.append(i)

for i in range(52):
    values.append(i+1)
    
# lists to dictionary
mapping_dict = {mapping_lists[i]: values[i] for i in range(len(mapping_lists))}

# get the values from mapping dictionary
priority_item_values = []

for entries in common_item:
    priority_item_values.append(mapping_dict[entries])

print(sum(priority_item_values))
    
#%% --- Day 3: Rucksack Reorganization --- Part 2

badges = []
# collect three lines and find intersection
for runs in range(1,int(len(data)/3)+1):
    group = data[3*(runs-1) : 3*(runs-1)+3]
    badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
    badges.append(badge)
    
sum_of_badges = []
# lookup values of badges
for entries in badges:
    sum_of_badges.append(mapping_dict[entries])

print(sum(sum_of_badges))
                     

    
