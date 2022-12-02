# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:40:50 2022
AOC 2022
Day 2

@author: Rahul
"""
#%% --- Day 2: Rock Paper Scissors --- Part 1

# Load data which is in text format
file = open('input','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# create a dictionary of points
points_lookup = {
    'A X':4,
    'B Y':5,
    'C Z':6,
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Z':9,
    'C X':7,
    'C Y': 2
    }

# loop through each entries, lookup the dictionary and keep adding points
total_points = 0

for entries in data:
    total_points += points_lookup[entries]



#%% --- Day 2: Rock Paper Scissors --- Part 2

# creating another map when X,Y,Z means lose, draw, win respectively
new_points_lookup = {
    'A X':3,
    'B Y':5,
    'C Z':7,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Z':9,
    'C X':2,
    'C Y': 6
    }

# loop through each entries, lookup the dictionary and keep adding points
total_points = 0

for entries in data:
    total_points += new_points_lookup[entries]
