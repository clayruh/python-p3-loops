#!/usr/bin/env python3
# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = print([height * 7920 for height in player_heights])

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
# happy_new_year()

def square_integers(int_list):
    squared_values = [abs(num * num) for num in int_list]
    return squared_values


def fizzbuzz():
    i = 1
    while i < 101:
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
fizzbuzz()