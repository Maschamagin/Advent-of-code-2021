"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 1: Sonar Sweep. 

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/1
-------------------------------------------------------------
"""
input_file = '/path/to/day1/input.txt'


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

print(count_depth_increasements(input_file))