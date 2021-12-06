# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:38:45 2021
Advent of Code 2021 is here
My goal is to attempt all challenges before the onset of 2022
@author: Rahul Venugopal
"""
#%% --- Day 4: Giant Squid --- Part 1

#test data
number_list = ['7','4','9','5','11','17','23','2','0','14','21','24','10','16','13','6','15','25','12','22','18','20','8','19','3','26','1']
cards = []
cards.append([['22', '13', '17', '11',  '0'], ['8',  '2', '23',  '4', '24'],['21', '9', '14', '16',  '7'], ['6', '10',  '3', '18',  '5'], ['1', '12', '20', '15', '19']])

cards.append([['3', '15',  '0',  '2', '22'], ['9', '18', '13', '17',  '5'],['19', '8','7','25','23'],['20', '11', '10', '24','4'],['14','21','16','12','6']])

cards.append([['14','21','17','24','4'],['10','16','15','9','19'],['18','8','23','26','20'],['22','11','13','6','5'],['2','0','12','3','7']])

# for column bingo check
number_list = ['22','8','21','6','1']
#%% Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# extract the bingo name list
number_string = data[0]
number_list = list(number_string.split(","))

# get all the bingo cards
cards = []

for card_no in range(2,601,6):
    cards.append(data[card_no:card_no+5])

for card_row in range(len(cards)):
    for card_col in range(5):
        cards[card_row][card_col] = cards[card_row][card_col].split()


print(len(cards))
# we got 100 bingo cards

import copy
copy_of_cards = copy.deepcopy(cards)
#%% taking first number from bingo list and checking if that number is there in every card in a loop and replacing if its a hit
  
bingo_nos = 0

lucky_card_all = []

lucky_no_row = []
lucky_no_col = []

while bingo_nos < len(number_list):    
    for bingo_card in range(len(cards)):
        take_a_card = cards[bingo_card]
        for rows in range(5):
            for columns in range(5):
                if take_a_card[rows][columns] == number_list[bingo_nos]:
                   take_a_card[rows][columns] = 'X'
        
        # checking if any rows has hit bingo
        for looper in range(len(take_a_card)):            
            if all(x == take_a_card[looper][0] for x in take_a_card[looper]):
                lucky_card_all.append(bingo_card)
                lucky_no_row.append(bingo_nos)
        
        # checking if any columns has hit bingo
        for second_looper in range(len(take_a_card)):            
            column_card = []
            for entries in range(len(take_a_card)):
                column_card.append([item[entries][:] for item in take_a_card])
                
            if all(y == column_card[second_looper][0] for y in column_card[second_looper]):
                    lucky_card_all.append(bingo_card)
                    lucky_no_col.append(bingo_nos)
        
        cards[bingo_card] = take_a_card            
        
    bingo_nos += 1

# find the min of first entries of lucky_card_row/col
# that is our lucky card
lucky_card = lucky_card_all[0]

#index of number just called
index_no_just_called = min(lucky_no_row[0], lucky_no_col[0])

# find the min of first entries of lucky_no_row/col
no_just_called = number_list[index_no_just_called]
#%% verifying
# load cards again
cards = copy_of_cards
lucky_bingo_card = cards[lucky_card]
bingo_nos = 0
while bingo_nos < index_no_just_called + 1:    
        for rows in range(5):
            for columns in range(5):
                if lucky_bingo_card[rows][columns] == number_list[bingo_nos]:
                   lucky_bingo_card[rows][columns] = 'X'
        bingo_nos += 1

# Replace substring in list of strings
lucky_bingo_card = [[item.replace('X', '0') for item in big_item] for big_item in lucky_bingo_card]

# converting all str to int
int_list = [[int(x) for x in lst] for lst in lucky_bingo_card]

# flatten the nested list
import itertools
flattened_list = list(itertools.chain(*int_list))

final_score_of_board = sum(flattened_list) * int(no_just_called)
print(final_score_of_board)

#%% --- Day 4: Giant Squid --- Part 2
# in previous part we were saving winning card no.s in lucky_card_all variable
# getting unique entries and checking the last entry should work

from collections import OrderedDict
fail_card_no = list(OrderedDict.fromkeys(lucky_card_all))[-1]

fail_card = copy_of_cards[fail_card_no]

bingo_nos = 0
trigger = 0

while trigger != 1: 
    for rows in range(5):
        for columns in range(5):
            if fail_card[rows][columns] == number_list[bingo_nos]:
               fail_card[rows][columns] = 'X'
               
    # checking if any rows has hit bingo
    for looper in range(len(fail_card)):            
        if all(x == fail_card[looper][0] for x in fail_card[looper]):
            trigger = 1            
    # checking if any columns has hit bingo
    for second_looper in range(len(fail_card)):            
        column_card = []
        for entries in range(len(fail_card)):
            column_card.append([item[entries][:] for item in fail_card])
            
        if all(y == column_card[second_looper][0] for y in column_card[second_looper]):
                trigger = 1
             
    bingo_nos += 1

# getting the final bingo entry
print(bingo_nos-1)
last_no_in_bingo = number_list[bingo_nos-1]   

# Replace substring in list of strings
fail_bingo_card = [[item.replace('X', '0') for item in big_item] for big_item in fail_card]

# converting all str to int
int_list = [[int(x) for x in lst] for lst in fail_bingo_card]

# flatten the nested list
import itertools
flattened_list = list(itertools.chain(*int_list))

final_score_of_board_failed = sum(flattened_list) * int(last_no_in_bingo)
print(final_score_of_board_failed)          
