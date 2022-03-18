"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 2: Dive.

For the complete puzzle description and to get your own input go to:
https://adventofcode.com/2021/day/2
-------------------------------------------------------------
"""
# -------------------------- Part 1 -------------------------------------
def position(input_file):
    '''
    Takes a file as input, reads every line into a list.
    '''
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    sum_forward = 0
    sum_down = 0
    sum_up = 0

    for line in input_lines:
        # makes input_lines a two-dimensional list: [['direction0', x], ['direction1', y] ...]:
        tmp = [s.replace(' ', '') for s in line.strip().split(' ')]

        if tmp[0] == 'forward':
            sum_forward += int(tmp[1])
        elif tmp[0] == 'down':
            sum_down += int(tmp[1])
        else:
            sum_up += int(tmp[1])

    horizontal_position = sum_forward
    depth_position = (sum_down - sum_up)

    # return the product of horizontal and depth position. That is the solution to the puzzle
    return horizontal_position*depth_position


# -------------------------- Part 2 -------------------------------------
def position2(input_file):
    '''
    Takes a file as argument, reads every line into a list.
    Then loops through that list to sum up all values for 'forward', 'up' and 'down'.
    Returns an integer.
    '''
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    sum_forward = 0
    aim = 0
    depth = 0

    for line in input_lines:
        # makes input_lines a two-dimensional list: [['direction0', x], ['direction1', y] ...]:
        tmp = [s.replace(' ', '') for s in line.strip().split(' ')]

        # now add up all steps in the different directions
        if tmp[0] == 'forward':
            sum_forward += int(tmp[1])
            depth += (int(tmp[1]) * aim)
        elif tmp[0] == 'down':
            aim += int(tmp[1])
        else:
            aim -= int(tmp[1])

    horizontal_position = sum_forward
    depth_position = depth

    # return product of horizontal and depth position. That is the solution to the puzzle
    return horizontal_position*depth_position

def main():
    '''
    main function to solve the puzzle
    '''
    input_file = '/day2/input.txt'
    print(position(input_file))
    print(position2(input_file))

if __name__ == '__main__':
    main()
