"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 2: Dive. 

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/1
-------------------------------------------------------------
"""

input_file = 'day2/input.txt'


def position(input_file):
    #open file and 
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    sum_forward = 0
    sum_down = 0
    sum_up = 0

    for line in input_lines:
        # create tmp list for every line in the file, first value is the command, second value is the steps
        tmp = [s.replace(' ', '') for s in line.strip().split(' ')]

        # now add up all steps in the different directions
        if(tmp[0] == 'forward'):
            sum_forward += int(tmp[1])
        elif(tmp[0] == 'down'):
            sum_down += int(tmp[1])
        elif(tmp[0] == 'up'):
            sum_up += int(tmp[1])

    horizontal_position = sum_forward
    depth_position = (sum_down - sum_up)

    # return the product of horizontal and depth position. That is the solution to the puzzle
    return horizontal_position*depth_position

print(position(input_file))    
