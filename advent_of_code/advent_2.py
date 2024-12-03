#!/usr/bin/env python

# Strategy: 
# 1) We first need to check if the report is "fluctuating" within safe limits. A report is considered fluctuating if 
#    the difference between each adjacent pair of values is between 1 and 3.
#    We check each adjacent pair, and if any pair does not meet this condition, the report is unsafe.
# 2) If the report passes the fluctuation check, we need to check if it is "ascending" ( each value is strictly greater
#    than the one before). If it is ascending, the report is safe.
# 3) If the report is not ascending, we check if it is descending (each value is strictly less than the one before). 
#    If it is descending, the report is safe.
# 4) If neither ascending nor descending, the report is unsafe. The goal is to count all reports that fulfill these conditions (safe reports).
# 5) Part 2: the Problem Dampener allows removing one value from the report to potentially make it safe. 
#    If removing any one value results in a safe report, the report is considered safe.

from util2 import read_input
# Process the raw input data into a list of reports (each report is a list of integers)
filepath = "../aoc_data/advent2-data.txt"
raw_reports = read_input(filepath)
reports = []
for line in raw_reports:
    numbers = list(map(int, line.split()))
    reports.append(numbers)

#print(reports)


# 1) Function to check if the report fluctuates safely (difference between adjacent numbers between 1 and 3)
def is_fluctuating (report):
    for i in range(len(report)-1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3:
            return False
    return True # differences are valid if between 1 and 3, so return safe (True)



# 2) Function to check if the report is strictly ascending
def is_ascending(report):
    for i in range(len(report) - 1):
        if report[i] >= report[i+1]: # if any value is greater than or equal to the next, it's not ascending
            return False
    return True
    

# 3) Function to check if the report is strictly descending
def is_descending (report):
    for i in range(len(report) - 1):
        if report[i] <= report[i+1]: # if any value is less than or equal to the next, it's not descending
            return False
    return True

# 4) Function to determine if the report is safe based on fluctuation and ascending or descending
def is_safe(report):
    if is_fluctuating(report) and (is_ascending(report) or is_descending(report)): # Report is safe if it fluctuates within the range of 1-3 and is either ascending or descending
        return True
    return False

# 5) Function to count how many reports are safe according to the is_safe function
def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report): # check if the current report is safe
            safe_count += 1
    return safe_count

print(count_safe_reports(reports))

# Part 2:
# Function to check if a report can be safe by removing one level (if it's not already safe)
def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    # Try removing each value one by one and check if the remaining report is safe
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:] # create a new report without the i-th element
        if is_safe(new_report): # if removing this element makes the report safe
            return True
    return False

# Function to count how many reports are safe with the Problem Dampener
def count_safe_reports_with_dampener(reports):
    safe_reports = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_reports += 1
    return safe_reports

print(count_safe_reports_with_dampener(reports))