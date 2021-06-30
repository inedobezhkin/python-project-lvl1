#!/usr/bin/env python

import prompt

def print_welcome():
    print('Welcome to the Brain Games!')

def greet_player():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

def main():
    print_welcome()
    greet_player()

if __name__ == '__main__':
    main()