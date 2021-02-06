from unittest.mock import patch
import random

def roll_dice():
    print("Rolling dice")
    return random.randint(1,6)

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"

@patch('__main__.roll_dice')
def test_guess_number(mocked_roll_dice):
    mocked_roll_dice.return_value = 1
    assert guess_number(1) == "You won!"
    assert guess_number(2) == "You lost!"


test_guess_number()