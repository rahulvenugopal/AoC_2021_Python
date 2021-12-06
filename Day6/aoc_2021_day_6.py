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
# that monent when you realise list won't save you


