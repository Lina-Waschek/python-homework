#!/usr/bin/env python

# Function to load the input from a file and return it as a list of strings
def load_input(filepath):
    with open(filepath, 'r') as infile:
        return [line.strip() for line in infile]
    
filepath = "../aoc_data/advent4-data.txt"
word_input = load_input(filepath)

# Make a counter to keep track of occurrences of "XMAS" and "SAMX"
count = 0

# Horizontal search (searching each row)
for row in word_input:
    count += row.count("XMAS")  
    count += row.count("SAMX") 

# Vertical search (searching columns)
# To search vertically, we need to transpose the matrix (make rows columns and columns rows)

transposed = [] # Empty list to store the transposed matrix

for i in range(len(word_input[0])): # go over the columns (from 0 to len of first row (all rows have the same length))
    new_row = ""  # for the new "column" as a row in the transposed matrix
    for row in word_input:  # For every row in the original matrix
        new_row += row[i]  # Add the character from column i to the new row (new column)
    transposed.append(new_row)  # Append the new column (now a row) to the transposed list

# Search in the vertical directions (same as in the vertical search but using the transposed matrix)
for col in transposed:
        count += col.count("XMAS")
        count += col.count("SAMX")

# Diagonal search (for both directions: left-to-right and right-to-left)
# Diagonals down (from left-top to right-bottom) 
diagonals_down = []
rows = len(word_input) # Get the number of rows 
cols = len(word_input[0]) # Get the number of columns 

for diag in range(rows + cols - 1):  # The number of diagonals is rows + cols - 1
    diagonal = ""
    for i in range(max(0, diag - cols + 1), min(diag + 1, rows)):# i is the row index
        j = diag - i  # j is the column index
        diagonal += word_input[i][j]
    diagonals_down.append(diagonal)

# and diagonals from right up to left down
diagonals_up = []

for diag in range(rows + cols - 1):
    diagonal = ""
    for i in range(max(0, diag - cols + 1), min(diag + 1, rows)):
        j = cols - 1 - (diag - i)  
        diagonal += word_input[i][j]
    diagonals_up.append(diagonal)

# search for the words like before
for diagonal in diagonals_down:
    count += diagonal.count("XMAS")
    count += diagonal.count("SAMX")

for diagonal in diagonals_up:
    count += diagonal.count("XMAS")
    count += diagonal.count("SAMX")

print(count)

# Part 2: find "X-MAS" shapes in the form of an "X" (two "MAS" arranged in an "X" shape) 
#counting XMAS shapes
def count_xmas_shapes(word_input):
    count_2 = 0
    rows_2 = len(word_input)
    cols_2 = len(word_input[0])

# checks if an "XMAS" shape exists in the matrix (around a given position (i, j))
# word_input[i][j] is the center
# word_input[i - 1][j - 1] is the character directly above and left of the center
# word_input[i + 1][j + 1] is the character directly below and right of the center
    def xmas(i, j):
        diag_a = word_input[i - 1][j - 1] + word_input[i][j] + word_input[i + 1][j + 1] # diagonal from the top-left to the bottom-right (consists of three characters "MAS" or "SAM")
        diag_b = word_input[i - 1][j + 1] + word_input[i][j] + word_input[i + 1][j - 1] # diagonal from the top-right to the bottom-left (consists of three characters "MAS" or "SAM")
        
        if (diag_a == "MAS" or diag_a == "SAM") and (diag_b == "MAS" or diag_b == "SAM"): #checks if both diag_a and diag_b are one of the two patterns "MAS" or "SAM"
            return True #if yes return True
        return False

    for i in range(1, rows_2 - 1): # each position in the matrix, but without the edges (first and last row, first and last column) because the X shape has no space at the edges
        for j in range(1, cols_2 - 1):
            if word_input[i][j] == 'A':  # checks if the character at the middle position (i, j) of the current iteration is an A
                if xmas(i, j):  # if an "XMAS" shape is found at this position
                    count_2 += 1 # the counter goes one up

    return count_2

xmas_shapes_count = count_xmas_shapes(word_input)
print(xmas_shapes_count)
    


