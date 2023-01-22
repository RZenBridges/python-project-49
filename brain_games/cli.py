#!/usr/bin/env python3
import prompt


def welcome_user():
    name = ''
    while name == '' or name.count(' ') > 0:
        name = prompt.string("May I have your name? No spaces: ")
    print(f"Hello, {name.capitalize()}!")
    return name
