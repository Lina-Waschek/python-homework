#!/usr/bin/env python

# 1) read the input
from util2 import read_input

def process_data(lines):
    # empty lists for ordering_rules und updates
    ordering_rules = []
    updates = []
    
    # go through each line to separate the rules and the updates
    for line in lines:
        line = line.strip()  # remove spaces
        if line == "":  # if the line is empty, skip it
            continue
        if "|" in line:  # if the line contains a "|"" it is an ordering rule
            a, b = map(int, line.split("|"))  # then split the line by "|"" and convert the parts to integers
            ordering_rules.append((a, b))  # add a, b to the ordering_rules list
        else:  # if the line is an update (has no "|"")
            update = list(map(int, line.split(",")))  # split the line by commas and convert the parts to integers
            updates.append(update)  # add the list of integers (update) to the updates list
    
    return ordering_rules, updates


filepath = "../aoc_data/advent5-data.txt"  
lines = read_input(filepath)
ordering_rules, updates = process_data(lines) 

#print(ordering_rules)
#print(updates)


# 1)check if the updates (the list of pages) follow the rules

def is_ordered(update): 
# create a dictionary (called position) to map each page in the update to its position in the list
    position = {}  # empty dictionary (key: page number, value: position of the page in the update)
    for i, page in enumerate(update):  # goes over every position and every page in updates   
        position[page] = i # assign the page's postion (index) to the page

    for a, b in ordering_rules: # for every pages pair in the ordering_rules
        if a in position and b in position: # if a and b are present in the update
            if position[a] > position[b]: # if page a comes after page b (a's position is larger than b's position)
                return False  # rule violated: a must come before b
    return True  # all rules are followed: the update is in the correct order

# 2) get the middle page number for all the correct updates
middle_sum = 0

def get_position(page): # to get the position to the page 
    return position[page]

for update in updates:
    if is_ordered(update):
       position = {}
       for i, page in enumerate(update):  # goes over every position and page in updates   
            position[page] = i # assign the page's postion (index) to the page

       sorted_update = sorted(update, key=get_position) # sort the pages in update based on their positions

       # get the middle page
       middle_index= len(sorted_update) // 2 # get the middle index by dividing the length of the sorted list by 2
       middle_number= sorted_update[middle_index] # get the corresponding page for the middle index

       middle_sum += middle_number

print(middle_sum)


# Part 2

# function to check if an update is already ordered according to the rules
def is_ordered(update):
    position = {}  # dictionary to store the position of each page in the update
    for i, page in enumerate(update):  # loop through each page and its index in the update
        position[page] = i  # store the index of the page in the position dictionary

    # check if the update follows all ordering rules
    for a, b in ordering_rules:
        if a in position and b in position:  # check if both pages a and b exist in the update
            if position[a] > position[b]:  # if page a comes after page b, the rule is violated
                return False  # update is not in the correct order
    return True  # update is in the correct order

# function to sort an update based on the ordering rules
def sort_update(update):
    sorted_update = update[:] # create a copy of the update list 
    swapped = True  

    # looping until no more swaps are needed and the list is fully sorted
    while swapped:
        swapped = False  
        for i in range(len(sorted_update) - 1):  # loop through the update list
            
            for a, b in ordering_rules: # check each pair of adjacent pages to see if they violate any ordering rules
                if sorted_update[i] == a and sorted_update[i + 1] == b: # the pair follows the rule
                    continue  # move on
                if sorted_update[i] == b and sorted_update[i + 1] == a: # if the pair violates the rule
                    sorted_update[i], sorted_update[i + 1] = sorted_update[i + 1], sorted_update[i] # swap the two pages
                    swapped = True  # swap has occurred
                    break  # exit after the swap
    return sorted_update  # return the sorted update

# Calculate the sum of the middle page numbers for the unsorted updates
middle_sum_part2 = 0  

for update in updates:
    if not is_ordered(update):  # only process unsorted updates
        sorted_update = sort_update(update)  # sort the update according to the rules
        middle_index = len(sorted_update) // 2  # get the middle index by dividing the length of the sorted list by 2
        middle_number = sorted_update[middle_index]  # get the corresponding page for the middle index
        middle_sum_part2 += middle_number  # add the middle page number to the total sum

print(middle_sum_part2)  