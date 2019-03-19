#!/bin/python3.7
# Simple Dice Roller for multiple dice types
# Part 1: Create a roll for a single dice type
# Part 2: Create a roll for multile dice types
# Part 3: Create rolls for multiple die and dice types
# Part 4: Record dice rolls for record
# Dice Types (sides) 4, 6, 8, 10, 12, and 20
import calc
diestate = calc.diestate

#Title
print("---------Dice Roller---------")
print("---------Let's get rollin!---------")
reroll = 'yes'
# prompt for dice type


while reroll == 'yes' or reroll == 'y':
    sides = diestate.sidesvalid("How Many Sides?")
    die = diestate.dievalid("How many Die?")
    roll = calc.info(sides, die)
    roll.default()
    rolls = []

    reroll = input("roll again? (yes/no)")
    if reroll == 'no' or reroll == 'n':
        print("---------Thanks for playing!---------")
        exit()
