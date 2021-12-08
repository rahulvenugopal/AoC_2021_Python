# -*- coding: utf-8 -*-
"""
Created on Sat Dec 7 10:38:45 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 7: The Treachery of Whales ---Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# creating integer list
crabs_horizontal_pos = list(data[0].split(","))
crabs_horizontal_pos = [int(i) for i in crabs_horizontal_pos]

import numpy as np
crabs_horizontal_pos = np.array(crabs_horizontal_pos)

from statistics import median
median_distances = round(median(crabs_horizontal_pos))

cheapest_route_fuel = sum(abs(crabs_horizontal_pos - median_distances))

#%% --- Day 7: The Treachery of Whales ---Part 2
# understanding crab engineering, mean might be the mid point for fuel
mean_point = round(np.mean(crabs_horizontal_pos))
    
cheapest_route_fuel_crabs = abs(crabs_horizontal_pos - mean_point)

total_fuel = 0

for crab_submarines in cheapest_route_fuel_crabs:
    total_fuel += (crab_submarines * (crab_submarines+1)) /2
    
# mean gets us to a value very close to answer. BUT
# we are actually minimising n*(n+1) /2

#%% Part 2 minimisation

total_fuel_estimates = []

for value in range(len(crabs_horizontal_pos)):    
    cheapest_route_fuel_crabs = abs(crabs_horizontal_pos - value)
    total_fuel = 0
    
    for crab_submarines in cheapest_route_fuel_crabs:
        total_fuel += (crab_submarines * (crab_submarines+1)) /2
        
    total_fuel_estimates.append(total_fuel)
    
print(min(total_fuel_estimates))

# I am still thinking about the range of values to iterate for optimisation
