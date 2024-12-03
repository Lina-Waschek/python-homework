#!/usr/bin/env python

# open the data as two lists 
# function spli_data: The function takes a text, splits it into lines, and then splits each line into two numbers. 
# These numbers are stored in two separate lists (left_list and right_list), and the function returns both of these lists.
def split_data(data):
    lines = data.strip().split("\n") # Split the input data into lines
    
    # Initialize empty lists for left and right values
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = line.split() # Split each line into two values
        
        left_list.append(int(left)) # Append the values to the respective lists
        right_list.append(int(right))
    
    return left_list, right_list

# Read the data from the file
with open("./advent1-data.txt", "r") as file:
    data = file.read()

# Call the function with the file content
left_list, right_list = split_data(data)


# Sort the lists
left_sorted = sorted(left_list)  # Sort the left list in ascending order
right_sorted = sorted(right_list)  # Sort the right list in ascending order

# Calculate the total distance
total_distance = 0
for l, r in zip(left_sorted, right_sorted):  # Pair elements from the two sorted lists
    if l > r:  # If the left number is bigger than the right number
        difference = l - r  # Calculate the difference
    else:  # If the right number is bigger than or equal to the left number
        difference = r - l  # Calculate the difference
    total_distance += difference  # Add the difference to the total distance

print(total_distance)

# Similarity score: count how many times each element from the left list appears in the right list,
# and then add the corresponding value to the similarity score
def calculate_similarity(left_list, right_list):
    total_similarity = 0
    
    for left in left_list:
        count_in_right = right_list.count(left) # Count how often the current element appears in the right list
        total_similarity += left * count_in_right # Add the product of the element and its count to the total similarity
    
    return total_similarity


# Calculate and print the similarity score
similarity_score = calculate_similarity(left_list, right_list)
print(similarity_score)