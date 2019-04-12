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
