"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 2: Dive. 

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/1
-------------------------------------------------------------
"""


# -------------------------- Part 1 -------------------------------------
def position(input_file):
    # open file and 
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    sum_forward = 0
    sum_down = 0
    sum_up = 0

    for line in input_lines:
        # create tmp list for every line in the file, first value is the direction, second value is the steps
        # e.g. the line 'forward 3' of the input file becomes the list ['forward', 3]. 
        # input_lines is now a two-dimensional list: [['direction0', x], ['direction1', y] ...]:
        tmp = [s.replace(' ', '') for s in line.strip().split(' ')]

        # now add up all steps in the different directions
        if(tmp[0] == 'forward'):
            sum_forward += int(tmp[1])
        elif(tmp[0] == 'down'):
            sum_down += int(tmp[1])
        else:
            sum_up += int(tmp[1])

    horizontal_position = sum_forward
    depth_position = (sum_down - sum_up)

    # return the product of horizontal and depth position. That is the solution to the puzzle
    return horizontal_position*depth_position


# -------------------------- Part 2 -------------------------------------
def position2(input_file):
    # open file and 
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    sum_forward = 0
    sum_down = 0
    sum_up = 0
    aim = 0
    depth = 0

    for line in input_lines:
        # create tmp list for every line in the file, first value is the direction, second value is the steps
        # e.g. the line 'forward 3' of the input file becomes the list ['forward', 3]. 
        # input_lines is now a two-dimensional list: [['direction0', x], ['direction1', y] ...]:
        tmp = [s.replace(' ', '') for s in line.strip().split(' ')]

        # now add up all steps in the different directions
        if(tmp[0] == 'forward'):
            sum_forward += int(tmp[1])
            depth += (int(tmp[1]) * aim)
        elif(tmp[0] == 'down'):
            aim += int(tmp[1])
        else:
            aim -= int(tmp[1])

    horizontal_position = sum_forward
    depth_position = depth

    # return the product of horizontal and depth position. That is the solution to the puzzle
    return horizontal_position*depth_position

def main():
    input_file = '/home/masch/Dokumente/Coding/Advent of Code/2021/day2/input.txt'
    return_value = position(input_file)
    print(position(input_file))
    print(position2(input_file))

if __name__ == '__main__':
    main() 