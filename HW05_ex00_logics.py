#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """

    while True:
        number = raw_input("Please enter an integer\n> ")
        try:
            number = int(number)
        except:
            print "Silly, that was not an integer!"
        else: 
            if number%2 == 0: 
                print 'You entered an even number.'
            else:
                print 'You entered an odd number.'
            return


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    beg_int = 1
    end_int = 100

    columns = 10
    rows = (end_int - beg_int + 1)/columns

    for i in range(rows):
        for j in range(columns):
            print beg_int, 
            beg_int = beg_int + 1
        print 

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    total = 0

    while True:
        x = raw_input("Please enter a number. Type 'done' when you would like the average.\n> ")
        if x == 'done':
            if count == 0:
                return 'We need some numbers to calculate an average!'
            return total/count
        try:
            x = float(x)
        except: 
            continue
        else:
            total = total + x
            count = count + 1

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """

    even_odd()
    ten_by_ten()
    print find_average()
    pass

if __name__ == '__main__':
    main()
