#!/usr/bin/env python3
import prompt


def welcome_user():
    name = ''
    while not name.strip():
        name = prompt.string("May I have your name? No spaces: ")
    print(f"Hello, {name.capitalize()}!")
    return name
