"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 3: Binary Diagnostic.

For the complete puzzle description and to get your own input go to:
https://adventofcode.com/2021/day/3
-------------------------------------------------------------
"""

# -------------------------- Part 1 -----------------------------------------

def power_consumption(input_file):
    '''
    function to calculate the power consumption rate.
    Takes a file as argument, splits each line into
    an element of a list and counts appearences of zeroes and ones in each index of every
    entry of that list.
    '''
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
            if elem[index] == '0':
                count_zeroes += 1
            else:
                count_ones += 1

        # set every index of gamma rate:
        if count_zeroes > count_ones:
            gamma_rate += '0'
        else:
            gamma_rate += '1'

         # reset counters
        count_zeroes = 0
        count_ones = 0

    # calculate epsilon rate:
    for i in range(0, len(gamma_rate)):
        if gamma_rate[i] == '0':
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'

    # multiply gamma rate and epsilon rate:
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

# -------------------------- Part 2 -----------------------------------------

def life_supprt_rating(input_file):
    '''
    function to calculate life support rate.
    Takes a file as argument, splits each line into
    an element of a list and counts appearences of zeroes and ones in each index of every
    entry of that list and sorts the respective elemets into a list for the detected ones,
    and a list for the detected zeroes.
    Whichever list has more elements in it, gets processed for thecalculation of
    the oxygen level, the other one gets deleted.
    For the CO2 level the other way around.
    '''
    # open file and create a list with lines as elements:
    with open(input_file,'r') as puzzle:
        input_lines = puzzle.read().splitlines()

    oxygen_generator_rating = input_lines
    oxygen_generator_rating_ones = []
    oxygen_generator_rating_zeroes = []
    co2_scrubber_rating = input_lines
    co2_scrubber_rating_zeroes = []
    co2_scrubber_rating_ones = []

    # Check every element for the appearance of either zero or one at each index.
    for index in range(0, len(oxygen_generator_rating[0])-1):
        for elem in oxygen_generator_rating:
            # Put elements in a list with the respective digit at that index:
            if elem[index] == '0':
                oxygen_generator_rating_zeroes.append(elem)
            else:
                oxygen_generator_rating_ones.append(elem)

        # replace list to loop through by list of elements with most common bit
        if len(oxygen_generator_rating_zeroes) > len(oxygen_generator_rating_ones):
            oxygen_generator_rating = oxygen_generator_rating_zeroes
        else:
            oxygen_generator_rating = oxygen_generator_rating_ones

        # clear temporary lists
        oxygen_generator_rating_zeroes = []
        oxygen_generator_rating_ones = []

        # when there is only one item left, break the loop
        if len(oxygen_generator_rating) == 1:
            break

    # Check every element for the appearance of either zero or one at each index.
    for index in range(0, len(co2_scrubber_rating[0])-1):
        for elem in co2_scrubber_rating:
            # Put elements in a list with the respective digit at that index:
            if elem[index] == '0':
                co2_scrubber_rating_zeroes.append(elem)
            else:
                co2_scrubber_rating_ones.append(elem)

        # replace list to loop through by list of elements with least common bit
        if len(co2_scrubber_rating_ones) < len(co2_scrubber_rating_zeroes):
            co2_scrubber_rating = co2_scrubber_rating_ones
        else:
            co2_scrubber_rating = co2_scrubber_rating_zeroes

        # clear temporary lists
        co2_scrubber_rating_zeroes = []
        co2_scrubber_rating_ones = []

        # when there is only one item left, break the loop
        if len(co2_scrubber_rating) == 1:
            break

    print(oxygen_generator_rating, co2_scrubber_rating)
    return int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)

def main():
    '''
    main function to solve the puzzle
    '''
    input_file = 'day3/input_day3.txt'
    print(power_consumption(input_file))
    print(life_supprt_rating(input_file))

if __name__ == '__main__':
    main()
