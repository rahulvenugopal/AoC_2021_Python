# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 11:14:45 2022
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 25: Sea Cucumber --- Part 1

# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()

# removing the empty line end
data = [line.rstrip() for line in data]

# creating bottom extra row and right most column for handling the shifts
data.append(data[0])

# creating one more column which is same as first column
appended_column = []

for entries in range(len(data)):
    appended_column.append(data[entries][-1])
    
for entries in range(len(data)):
    data[entries] = data[entries] + data[entries][0]
           
#%% east herd            
for row in range(len(data)-1):
    for column in range(len(data[0])-1):
        if (data[row][column] == '>' and data[row][column+1] == '.'):
            data[row][column] = '.'
            data[row][column+1] = '>'

# replacing first row with last row as a wrap around
data[0] = data[-1] 

# south herd            
for row in range(len(data)-1):
    for column in range(len(data[0])-1):
        if (data[row][column] == 'v' and data[row+1][column] == '.'):
            data[row][column] = '.'
            data[row+1][column] = 'v'

# replacing first column with last column as a wrap around
for        
            
        
    
    

# navigate the suth herd
