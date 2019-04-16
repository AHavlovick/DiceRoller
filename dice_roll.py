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
    if int(self.value) in facetypes:
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

class UserInput:
  def __init__(self):
    self.invalidnum = 'That is not a valid number'

  def faceinput(self):
    while True:
      faces = input('How many Faces?')
      ds = Diestate(faces)
      if ds.validinteger() == False:
        print(self.invalidnum)
      elif ds.validface() == False:
        print('Choose 4, 6, 8, 10, 12, or 20')
      else:
        return faces
    return faces

  def diceinput(self):
    while True:
      dice = input('How many Dice?')
      ds = Diestate(dice)
      if ds.validinteger() == False:
        print(self.invalidnum)
      else:
        return dice
    return dice

reroll = 'yes'
while reroll == 'yes' or reroll == 'y':
  ui = UserInput()
  faces = int(ui.faceinput())
  dice = int(ui.diceinput())
  result = DiceRoller(Dice(faces)).roll(dice)
  print(*result, sep=' + ')
  print(sum(result))

  reroll = input('roll again? (yes/no)')
  if reroll == 'no' or reroll == 'n':
    exit()
