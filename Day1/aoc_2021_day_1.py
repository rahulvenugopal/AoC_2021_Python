# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:27:51 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 1: Sonar Sweep --- Part 1

# Load data which is in text format
file = open('input1.txt','r')
data = file.readlines()

# converting string to int using map
data_numbers = list(map(int,data))

def depth_checker(data_numbers):

    # initialising a list for stroring inc or dec
    depth_meter = ['N/A - no previous measurement']

    # entering a loop
    for depths in range(len(data_numbers)-1):

        if data_numbers[depths+1] > data_numbers[depths]:
            depth_meter.append('inc')

        elif data_numbers[depths+1] < data_numbers[depths]:
            depth_meter.append('dec')

        elif data_numbers[depths+1] == data_numbers[depths]:
            depth_meter.append('no change')

    # counting things
    print(depth_meter.count('inc'))

    #import Counter
    from collections import Counter
    return Counter(depth_meter)

depth_checker(data_numbers)

#%% --- Day 1: Sonar Sweep --- Part 2
# create a new list bysumming three entries and sliding the window
serial_depths = []

# create a loop that runs n-3
for depths in range(len(data_numbers)-2):
    new_depth = data_numbers[depths] + data_numbers[depths+1] + data_numbers[depths+2]
    serial_depths.append(new_depth)

depth_checker(serial_depths)