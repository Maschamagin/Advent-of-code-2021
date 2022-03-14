"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 1: Sonar Sweep. 

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/1
-------------------------------------------------------------
"""
input_file = '/path/to/day1/input.txt'

#---------------- part 1 --------------------------
def count_depth_increasements(input):
    # Count for number of times the depth of sonar increases - will be returned later:
    depth_increase_count = 0

    # Open puzzle input and read lines into a list
    with open(input,'r') as fin:
        lines = fin.readlines()

    first_value = 0

    # compare each item of list with the one before, update depth_increase_count:
    for line in lines:
        if(int(line.strip()) > first_value):
            depth_increase_count += 1
        first_value = int((line.strip()))

    # First element in list is always greater than first_value at first assignment (which is 0). Therefore, return count - 1:
    return depth_increase_count - 1


# ----------------------- Part 2 --------------------------------
def count_depth_increasment_shifting_window(input, windowsize):
    sum_of_entries_in_shifting_window = []
    depth_increase_count_shifting_window = 0

    with open(input,'r') as puzzle:
        lines = puzzle.readlines()
    for k in  range (0, len(lines)):
        lines[k] = int(lines[k]) 

    sum = 0
    for i in range(len(lines) - windowsize + 1 ):
        for j in range (0, windowsize):
            sum += lines[i+j]
        sum_of_entries_in_shifting_window.append(sum)
        sum = 0
    
    depth_increase_count = 0
    first_value = 0  

    for elem in range (0, len(sum_of_entries_in_shifting_window)):
        if(sum_of_entries_in_shifting_window[elem] > first_value):
            depth_increase_count += 1
        first_value = sum_of_entries_in_shifting_window[elem] 
    return depth_increase_count - 1

print(count_depth_increasements(input_file))
print(count_depth_increasment_shifting_window(input_file, 3))
