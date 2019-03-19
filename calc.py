#!/bin/python3.7

import random
randint = random.randint
sidetypes = [4, 6, 8, 10, 12, 20]
rolls = []
# Roll Calculator
class info():
    def __init__(self, sides, die):
        self.sides = sides
        self.die = die

    def default(self):
        for x in range(self.die):
            rolls.append(randint(1, self.sides))
            if x == self.die:
                break
            x = x + 1
        print(" + ".join(str(x) for x in rolls))
        print(sum(rolls))

# Input Validation
class diestate():
    def sidesvalid(self):
        while True:
            try:
                value = int(input(self))
            except ValueError:
                print ('Sorry, that is not a number')
                continue

            if value in sidetypes:
                break
            else:
                print ('Please choose 4, 6, 8, 10, 12, or 20')
        return value

    def dievalid(self):
        while True:
            try:
                value = int(input(self))
            except ValueError:
                print ('Sorry, that is not a number')
            else:
                break
        return value
