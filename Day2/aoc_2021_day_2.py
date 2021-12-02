# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:57:06 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 2: Dive! --- Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()

# there was a line break, getting rid of that
data = [line.rstrip() for line in data]

# calculating the planned course of submarine
def navigation_prog(data):

    position = 0
    depth = 0

    for steps in range(len(data)):
        pos = data[steps].split (" ")[0]
        dist = int(data[steps].split (" ")[1])

        if pos == 'forward':
            position += dist

        elif pos == 'down':
            depth += dist

        elif pos == 'up':
            depth -= dist

    return position,depth, position*depth

navigation_prog(data)

#%% --- Day 2: Dive! --- Part 2
# calculating the updated planned course of submarine
def navigation_prog_new(data):

    position = 0
    depth = 0
    aim = 0

    for steps in range(len(data)):
        pos = data[steps].split (" ")[0]
        dist = int(data[steps].split (" ")[1])

        if pos == 'forward':
            position += dist
            depth = depth + (aim * dist)

        elif pos == 'down':
            aim += dist

        elif pos == 'up':
            aim -= dist

    return position,depth,aim, position*depth

navigation_prog_new(data)
