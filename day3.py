"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 3: Binary Diagnostic.

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/1
-------------------------------------------------------------
"""

def power_consumption(input_file):
    # open file and create a list with lines as elements:
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()
    
    count_zeroes = 0
    count_ones = 0
    gamma_rate = ''
    epsilon_rate = ''

    # for each index of every element, count the appearences of zeroes and ones: 
    for index in range(0, len(input_lines[0])-1):
        for elem in input_lines:
            if (elem[index] == '0'):
                count_zeroes += 1
            else:
                count_ones += 1

        # set gamma rate for every index:
        if (count_zeroes > count_ones):
            gamma_rate += '0'
        else:
            gamma_rate += '1'

         # reset counters
        count_zeroes = 0
        count_ones = 0
    
    # calculate epsilon rate: 
    for i in range(0, len(gamma_rate)):
        if (gamma_rate[i] == '0'):
            epsilon_rate += '1'
        else: 
            epsilon_rate += '0'
    
    # multiply gamma rate and epsilon rate:
    return (int(gamma_rate, 2) * int(epsilon_rate, 2))


def main():
    input_file = 'day3/input_day3.txt'
    print(power_consumption(input_file))

if __name__ == '__main__':
    main() 

    

        
    
            

