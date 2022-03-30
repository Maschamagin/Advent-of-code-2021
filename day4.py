"""
-------------------------------------------------------------
Solution for Advent of Code 2021 Day 4: Giant Squid

For the complete puzzle description and to get your own input go to: 
https://adventofcode.com/2021/day/4
-------------------------------------------------------------
"""

def read_input_file (input_file):
    '''
    Takes a txt file als input and reads every line into a list. 
    Then some modificaations: Pop out the numbers to play the game with (drawn_numbers),
    write all Bingo cards (every five elements of the list) together as an element 
    into a new list (bingo_cards), remove whitespaces and newline characters, and 
    finally return drawn_numbers along with the bingo cards as a list.
    '''
    with open (input_file, encoding="utf-8") as puzzle:
        input_lines = puzzle.read().splitlines()

    # filter out numbers that are played (first line in input file)
    drawn_numbers = input_lines.pop(0).split(' ')
    drawn_numbers = drawn_numbers[0].split(',')

    # Delete now first blank line in file 
    input_lines.pop(0)
    
    bingo_cards = [[]]

    for line in input_lines:
        if len(line) > 0:
                # remove whitespace at beginning of the line at one-digit numbers
                line = line.lstrip()
                # remove double whitespace at one-digit numbers in file
                line = line.replace('  ', ' ')
                row = line.split(' ')
                bingo_cards[-1].append(row)
        # Every blank line (length == 0) gives the signal to open next element in list  
        else:
            bingo_cards.append([])

    return bingo_cards, drawn_numbers

def play_bingo(bingo_cards, drawn_number):
    '''
    Takes a list of strings of numbers (for the player's cards) 
    and the string of a number as arguments,
    and tags the drawn number with an 'x' on the Bingo card. 
    Returns the bingo_cards with tagged numbers. One element of the 
    returned list might look like this:
    [['91', '72x', '10', '32', '20'], 
    ['23', '18', '44x', '78', '6'], 
    ['46', '36', '77', '60x', '75'], 
    ['47x', '49', '16x', '89', '8'], 
    ['2', '95', '48x', '38', '85']]
    '''
    for card in bingo_cards:
        for row in card:
            if drawn_number in row:
                row[row.index(drawn_number)] += 'x'
    return bingo_cards


def check_for_bingo(bingo_cards):
    '''
    Checks if every element in a list has an 'x'. 
    The arguement bingo_card is a list, that contains lists of 5 lists of 5 elements.
    One element of the bingo_cards argument might look like this:
    [['91', '72x', '10', '32', '20'], 
    ['23', '18', '44x', '78', '6'], 
    ['46', '36', '77', '60x', '75'], 
    ['47x', '49', '16x', '89', '8'], 
    ['2', '95', '48x', '38', '85']]
    This function checks, if either in a row or in a column, 
    every number is tagged with an 'x' and returns that card along with a boolean. 
    Returns None if no Bingo is found. 
    '''
    bingo_in_row = False
    bingo_in_column = False
    for card in bingo_cards:
        for row in card:
            bingo_in_row = all('x' in elem for elem in row)
            if bingo_in_row:
                return card, bingo_in_row, bingo_cards.index(card)
            
    
    for card in bingo_cards:
        for column in range(0,len(card)):
            bingo_in_column = all('x' in card[row][column] for row in range(0,len(card[0])))
            if bingo_in_column:
                return card, bingo_in_column, bingo_cards.index(card)

def check_and_pop(card):
    '''
    Function to check if a bingo appears in a card. 
    One card might look like this:
    [['91', '72x', '10', '32', '20'], 
    ['23', '18', '44x', '78', '6'], 
    ['46', '36', '77', '60x', '75'], 
    ['47x', '49', '16x', '89', '8'], 
    ['2', '95', '48x', '38', '85']]
    The variable bingo turns true, if either every number of a row, 
    or every number in one column contains an 'x'.
    Returns True if bingo is True and None if no bingo was detected.
    '''
    bingo = False
    for row in card:
        bingo = all('x' in elem for elem in row)
        if bingo:
            return bingo

  
    for column in range(0,len(card)):
        bingo = all('x' in card[row][column] for row in range(0,len(card[0])))
        if bingo:
            return bingo


def retrieve_winning_numbers(card):
    '''
    A function to create a list of the winning numbers of a bingo card,
    and a list of unhit numbers of this card that has a bingo.
    Argument is a list of lists of strings, return values are
    two lists of integers.
    '''
    numbers_of_winning_card_hit = []
    numbers_of_winning_card_unhit = []
    for row in card:
        for number in row:
            if 'x' in number:
                number = number.replace('x','') # remove the 'x'-tag
                numbers_of_winning_card_hit.append(int(number))
            else: 
                numbers_of_winning_card_unhit.append(int(number))
    return numbers_of_winning_card_hit, numbers_of_winning_card_unhit

def main():
    '''
    The main function to solve the giant squid bingo puzzle.
    First, it retrieves a list of strings of numbers that are going to be played 
    out of the read input file function. 
    For every drawn number (given as read_input_file[1]),
    it calls the play bingo and check for bingo function,
    until it finds the first actual bingo.
    Prints the sum of all numbers in the winning card that were not hit during previous rounds,
    times the value of the last number drawn during the game.
    '''
    input_file = 'day4/input_day4.txt'
    arguments = (read_input_file(input_file))
    arguments_lose = (read_input_file(input_file))
    last_number_drawn = 0

    # iterate through all drawn numbers until first bingo is detected:
    for elem in arguments[1]: # arguments[1] is a list of the numbers drawn during the game
        bingo = check_for_bingo(play_bingo(arguments[0], elem)) 
        last_number_drawn = int(elem)
        if bingo:
            break

    winning_card = retrieve_winning_numbers(bingo[0])
    print(sum(winning_card[1])*last_number_drawn) # solution to the puzzle part 1

    # iterate through all drawn numbers and delete all cards that win, until only one card remains:
    for elem in arguments_lose[1]:
        last_number_drawn = int(elem)
        bingo_cards = play_bingo(arguments_lose[0], elem)
        for card in bingo_cards:
            bingo = check_and_pop(card)
            if bingo:
                bingo_cards.remove(card)
        if len(bingo_cards) == 1:
            break 
    
    losing_card = retrieve_winning_numbers(bingo_cards[0])
    print(sum(losing_card[1])*last_number_drawn) # solution to the puzzle part 2

if __name__ == '__main__':
    main()
