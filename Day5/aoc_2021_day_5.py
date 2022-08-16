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

#%%

# throwing away the arrow
for locs,lines in enumerate(data):
    data[locs] = lines.replace(' -> ', ',')

# making a list of integers for x1,y1,x2,y2
for locs, entries in enumerate(data):
    data[locs] = list(map(int, entries.split(",")))

# Bresenham algorithm gets us coordinates of all points between two points
from bresenham import bresenham
import matplotlib.pyplot as plt
from itertools import chain
from collections import Counter
import numpy as np

coordinates_vents = []
for locs, coordinates in enumerate(data):
    coordinates_vents.append(list(bresenham(*data[locs])))

# getting all x and y locations of points
xs = [[x[0] for x in set1] for set1 in coordinates_vents]
ys = [[x[1] for x in set1] for set1 in coordinates_vents]

xs = list(chain(*xs))
ys = list(chain(*ys))

plt.plot(xs, ys, 'steelblue', alpha = 0.8)
plt.show()

# merging xs and ys as tuple
all_points_spots = tuple(zip(xs, ys))

unique_counts = Counter(chain(all_points_spots))
counts_of_points_overlap = np.array(list(unique_counts.values()))

print(sum(counts_of_points_overlap >= 2))

