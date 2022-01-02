# -*- coding: utf-8 -*-
"""
Created on Fri Dec  21 11:02:08 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 21: Dirac Dice --- Part 1

# get the starting position
player_1_pos = 7
player_2_pos = 2

player_1_score = 0
player_2_score = 0

dice_runs = list(range(1,101))*100

# initialise runs
runs = 0

while player_1_score < 1000 and player_2_score < 1000:
    if player_1_pos + sum(dice_runs[runs:runs+3]) < 11:
        player_1_pos = player_1_pos + sum(dice_runs[runs:runs+3])
    elif (player_1_pos + sum(dice_runs[runs:runs+3])) % 10 ==0:
        player_1_pos = 10
    else:
        player_1_pos = (player_1_pos + sum(dice_runs[runs:runs+3])) % 10
        
    player_1_score += player_1_pos
    runs += 3

    if player_1_score < 1000 and player_2_score < 1000:
        if player_2_pos + sum(dice_runs[runs:runs+3]) < 11:
            player_2_pos = player_2_pos + sum(dice_runs[runs:runs+3])
        elif (player_2_pos + sum(dice_runs[runs:runs+3])) % 10 ==0:
            player_2_pos = 10
        else:
            player_2_pos = (player_2_pos + sum(dice_runs[runs:runs+3])) % 10
        player_2_score += player_2_pos
        runs += 3    
    

print('Total runs is',runs)
print('Player 1 scored', player_1_score)
print('Player 2 scored',player_2_score)

print(runs*player_2_score)

#%% --- Day 21: Dirac Dice --- Part 2



