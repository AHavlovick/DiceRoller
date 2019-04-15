import dice_roll
import unittest

class TestDice(unittest.TestCase):
  """
  Test the roll functionality
  """

  def test_single_roll(self):
    d = dice_roll.Dice(6)
    t = d.roll()
    self.assertTrue(1<=t and t<=6)

class TestDiceRoller(unittest.TestCase):
  """
  Test multiple roll functionality
  """

  def test_multi_roll(self):
    d = dice_roll.DiceRoller(dice_roll.Dice(6))
    t = d.roll(4)
    self.assertTrue(len(t) == 4)

class TestInvalidInputLetter(unittest.TestCase):
  """
  Test roll with non-numerical character
  """
  def test_input_letter(self):
    d = dice_roll.Diestate('a')
    t = d.validinteger()
    self.assertTrue(t == False)

class TestInvalidInputFloat(unittest.TestCase):
  """
  Test input with Float
  """
  def test_input_float(self):
    d = dice_roll.Diestate(5.6)
    t = d.validinteger()
    self.assertTrue(t == False)

class TestInvalidInputNegative(unittest.TestCase):
  """
  Test input with negative number
  """
  def test_input_negative(self):
    d = dice_roll.Diestate(-4)
    t = d.validinteger()
    self.assertTrue(t == False)

class TestInvalidFaceSelction(unittest.TestCase):
  """
  Test face input in acceptable facetypes
  """
  def test_invalid_face(self):
    d = dice_roll.Diestate(7)
    t = d.validface()
    self.assertTrue(t == False)
