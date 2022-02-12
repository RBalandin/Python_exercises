#!/usr/bin/env python3

import random


def guess_a_number():
    number = random.randint(0, 99)
    print('I have guessed a number, try to find it')
    print('To exit type 101')

    while True:
        n = int(input('Write a number and press Enter: '))
        if n == number:
            print('You are the winner')
            return
        elif n == 101:
            print('Bye')
            return
        elif n < number:
            print('May be some more')
        elif n > number:
            print('May be a little less')
        else:
            continue

if __name__ == '__main__':
    guess_a_number()


