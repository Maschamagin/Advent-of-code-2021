"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 3: Binary Diagnostic.

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/3
-------------------------------------------------------------
"""

#----------------------------------------------------------------------------
# -------------------------- Part 1 -----------------------------------------
# ---------------------------------------------------------------------------

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

        # set every index of gamma rate:
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


#----------------------------------------------------------------------------
# -------------------------- Part 2 -----------------------------------------
# ---------------------------------------------------------------------------


def life_supprt_rating(input_file):
    # open file and create a list with lines as elements:
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.readlines()

    oxygen_generator_rating = input_lines
    oxygen_generator_rating_ones = []
    oxygen_generator_rating_zeroes = []
    CO2_scrubber_rating = input_lines
    CO2_scrubber_rating_zeroes = []
    CO2_scrubber_rating_ones = []

    # calculate oxygen generator rating:
    # Check every element for the appearance of either zero or one at each index. 
    # if it is a zero, append to list of all elements with zeroes at this specific index,
    # if it is a one, act accordingly.
    for index in range(0, len(oxygen_generator_rating[0])-1):
        for elem in oxygen_generator_rating:
            if (elem[index] == '0'):
                oxygen_generator_rating_zeroes.append(elem)
            else:
                oxygen_generator_rating_ones.append(elem)
                
        # if there are more zeroes than ones at one pecific index, next iteration starts with 
        # the elements with the most common bit, which are all in the zero-list:
        if (len(oxygen_generator_rating_zeroes) > len(oxygen_generator_rating_ones)):
            oxygen_generator_rating = oxygen_generator_rating_zeroes
        else: 
            oxygen_generator_rating = oxygen_generator_rating_ones

        # clear temporary lists
        oxygen_generator_rating_zeroes = []
        oxygen_generator_rating_ones = []

        # when there is only one item left, break the loop
        if(len(oxygen_generator_rating) == 1):
            break

    # calculate CO2 scrubber rating:
    # Check every element for the appearance of either zero or one at each index. 
    # if it is a zero, append to list of all elements with zeroes at this specific index,
    # if it is a one, act accordingly.
    for index in range(0, len(CO2_scrubber_rating[0])-1):
        for elem in CO2_scrubber_rating:
            if (elem[index] == '0'):
                CO2_scrubber_rating_zeroes.append(elem)
            else:
                CO2_scrubber_rating_ones.append(elem)
                
        # if there are less ones than zeroes at one pecific index, next iteration starts with 
        # the least common bit, which is then the zero-list:
        if (len(CO2_scrubber_rating_ones) < len(CO2_scrubber_rating_zeroes)):
            CO2_scrubber_rating = CO2_scrubber_rating_ones
        else: 
            CO2_scrubber_rating = CO2_scrubber_rating_zeroes

        # clear temporary lists
        CO2_scrubber_rating_zeroes = []
        CO2_scrubber_rating_ones = []
        
        # when there is only one item left, break the loop
        if(len(CO2_scrubber_rating) == 1):
            break

    print(oxygen_generator_rating, CO2_scrubber_rating)
    return int(oxygen_generator_rating[0], 2) * int(CO2_scrubber_rating[0], 2)




def main():
    input_file = 'day3/input_day3.txt'
    print(power_consumption(input_file))
    print(life_supprt_rating(input_file))

if __name__ == '__main__':
    main()
