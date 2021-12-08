# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:38:45 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 6: Lanternfish --- Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# extract the ages of each lantern fish
age_lantern_list = list(data[0].split(","))
age_lantern_list = [int(i) for i in age_lantern_list]

days = 0
while days <256:
    for fishes in range(len(age_lantern_list)):
        if age_lantern_list[fishes] != 0 :
            age_lantern_list[fishes] = age_lantern_list[fishes] - 1
        else:
            age_lantern_list[fishes] = 6
            age_lantern_list.append(8)
    
    days += 1
    
len(age_lantern_list)

#%% #%% --- Day 6: Lanternfish --- Part 2
# that moment when you realise creating lots of lantern fishes won't save you

# create an array to keep track of count of lanterns fish of different ages
import numpy as np

# test lantern_age_array = np.array([0,1,1,2,1,0,0,0,0])

lantern_age_array = np.array(age_lantern_list)

from collections import Counter
count_ages_lantern_fishes = Counter(lantern_age_array)

#%% getting the sorted values as an array of 0-8
import numpy as np
lantern_age_array = np.array([0,193,29,27,25,26,0,0,0],dtype='int64')

for days in range(256):
    lantern_age_array = np.roll(lantern_age_array,-1)
    if lantern_age_array[8] != 0:
        lantern_age_array[6] += lantern_age_array[8]
    print(days)
    print(sum(lantern_age_array))