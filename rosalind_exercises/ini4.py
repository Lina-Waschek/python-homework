# Problem INI4 - Conditions and Loops

# Description:
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Steps:
# 1) from a to b
# range(a, b+1)

# 2) is the number odd
# x % 2 == 1

# 3) add it if odd
# sum_of_odds = sum_of_odds + x

# Code answer:
a= 4297
b= 8720 
sum_of_odds=0 #the start value for the sum is 0

for x in range(a, b+1): #loop from a to b
    if x % 2 == 1: #is the number odd
        sum_of_odds = sum_of_odds + x #if odd add to the sum

print (sum_of_odds) #print the result

# Answer: 14395696