# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:02:08 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 3: Binary Diagnostic --- Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()

# there was a line break, getting rid of that
data = [line.rstrip() for line in data]

def binary_program(data):
    # finding power consumption
    gamma_rate = []
    from collections import Counter

    for digits in range(len(data[0])):
        msb = []
        for entries in range(len(data)):
            msb.append(data[entries][digits])

        dict = Counter(msb)
        gamma_rate.append(max(dict, key=dict.get))

    gamma = ''.join(gamma_rate)
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

    return(int(gamma,2), int(epsilon,2), int(gamma,2) * int(epsilon,2))

#%% --- Day 3: Binary Diagnostic --- Part 2
# oxygen generator rating
from collections import Counter
numbers = []
oxygen_rating = []
length = len(data[0])

for digits in range(length):

    msb = []

    for entries in range(len(data)):
        msb.append(data[entries][0])

    dict = Counter(msb)
    number_to_retain = max(dict, key=dict.get)

    if len(dict) == 2:
        items_in_dict = iter(dict.values())
        zeros = next(items_in_dict)
        ones = next(items_in_dict)

        if zeros == ones:
            number_to_retain = '1'

    oxygen_rating.append(number_to_retain)
    data = [nos for nos in data if nos.startswith(number_to_retain)]

    for items in range(len(data)):
        data[items] =  data[items][1:]

o2 = ''.join(oxygen_rating)
oxygen = int(o2,2)

# CO2 scrubber rating
file = open('input.txt','r')
data = file.readlines()
# there was a line break, getting rid of that
data = [line.rstrip() for line in data]

from collections import Counter
numbers = []
co2_rating = []
length = len(data[0])

for digits in range(length):

    msb = []

    for entries in range(len(data)):
        msb.append(data[entries][0])

    dict = Counter(msb)
    number_to_retain = min(dict, key=dict.get)

    if len(dict) == 2:
        items_in_dict = iter(dict.values())
        zeros = next(items_in_dict)
        ones = next(items_in_dict)

        if zeros == ones:
            number_to_retain = '0'

    co2_rating.append(number_to_retain)
    data = [nos for nos in data if nos.startswith(number_to_retain)]

    for items in range(len(data)):
        data[items] =  data[items][1:]

co2 = ''.join(co2_rating)
carbondioxide = int(co2,2)

print(oxygen*carbondioxide)
