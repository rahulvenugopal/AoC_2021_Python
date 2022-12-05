# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:16:48 2022
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 5: Hydrothermal Venture --- Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# create a square array lists with all zeros

import numpy as np
grid_of_vents = np.zeros((999,999))

for indices,entries in enumerate(data)  :
    print(indices)
    x1,y1 = entries.split('->')[0].rstrip().lstrip().split(',')
    x2,y2 = entries.split('->')[1].rstrip().lstrip().split(',')

    if x1 == x2 and y1 != y2:
        to_fill = list(range(min(int(y1), int(y2)), max(int(y1), int(y2))+1))

        # add 1 to indicate vent locations
        for entries in to_fill:
            grid_of_vents[entries][int(x1)] = grid_of_vents[entries][int(x1)] + 1

    if y1 == y2 and x1 != x2:
        to_fill = list(range(min(int(x1), int(x2)), max(int(x1), int(x2))+1))

        # add 1 to indicate vent locations
        for entries in to_fill:
            grid_of_vents[int(y1)][entries] = grid_of_vents[int(y1)][entries] + 1

# count indices in grid which are greater than 2
counter = 0

for rows in range(len(grid_of_vents)):
    for columns in range(len(grid_of_vents)):
        if grid_of_vents[rows][columns] >1:
            counter += 1

print("Points with atleast two lines cross is " + str(counter))

#%% --- Day 5: Hydrothermal Venture --- Part 2

# taking on-diagonal and off diagonal vents too

# create a square array lists with all zeros

import numpy as np
grid_of_vents = np.zeros((999,999))

for indices,entries in enumerate(data)  :
    print(indices)
    x1,y1 = entries.split('->')[0].rstrip().lstrip().split(',')
    x2,y2 = entries.split('->')[1].rstrip().lstrip().split(',')

    if x1 == x2 and y1 != y2:
        to_fill = list(range(min(int(y1), int(y2)), max(int(y1), int(y2))+1))

        # add 1 to indicate vent locations
        for entries in to_fill:
            grid_of_vents[entries][int(x1)] = grid_of_vents[entries][int(x1)] + 1

    if y1 == y2 and x1 != x2:
        to_fill = list(range(min(int(x1), int(x2)), max(int(x1), int(x2))+1))

        # add 1 to indicate vent locations
        for entries in to_fill:
            grid_of_vents[int(y1)][entries] = grid_of_vents[int(y1)][entries] + 1

    if x1 ==x2 and y1 == y2:
        to_fill = list(range(min(int(x1), int(y1)), max(int(x2), int(y2))+1))

        # add 1 to indicate vent locations
        for entries in to_fill:
            grid_of_vents[entries][entries] = grid_of_vents[entries][entries] + 1

    if abs(int(x1) + int(x2)) == abs(int(y1)-int(y2)):
        to_fill_xs = list(range((min(int(x1), int(x2))), max(int(x1), int(x2)) +1))
        to_fill_ys = list(reversed(to_fill_xs))

        # add 1 to indicate vent locations
        for indices in range(len(to_fill_xs)):
            grid_of_vents[to_fill_xs[indices]][to_fill_ys[indices]] = grid_of_vents[to_fill_xs[indices]][to_fill_ys[indices]] + 1


# count indices in grid which are greater than 2
counter = 0

for rows in range(len(grid_of_vents)):
    for columns in range(len(grid_of_vents)):
        if grid_of_vents[rows][columns] >1:
            counter += 1

print("Points with atleast two lines cross is " + str(counter))

#%%

data = [
        '0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2']
