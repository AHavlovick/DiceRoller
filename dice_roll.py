from random import randint

class Diestate:
  def __init__(self, value):
    self.value = value

  def validinteger(self):
    try:
      test = int(self.value)
    except ValueError:
      return False
    else:
      if test < 1 or isinstance(self.value, float):
        return False
      else:
        return True

  def validface(self):
    facetypes = [4, 6, 8, 10, 12, 20]
    if self.value in facetypes:
      return True
    else:
      return False

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
