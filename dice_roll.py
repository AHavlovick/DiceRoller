from random import randint

class Dice:
	def __init__(self, faces):
		self.faces = faces

	def roll(self):
		return randint(1, self.faces)

class DiceRoller:
  def __init__(self, dice):
    self.dice = dice

  def roll(self, count):
    rolls = []
    for x in range(count):
      rolls.append(self.dice.roll())
    return rolls
