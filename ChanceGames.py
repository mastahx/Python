import random

money = 100

#----------------------------------[         coin flip bet       ]----------------------------------
def flip_coin(guess, bet):
    global money
    coinside = random.randint(1,2)
    if coinside == 1 and (guess == 'tails' or guess == 'heads'):
        money += bet
        return "You won $" + str(bet)
    elif coinside != 1 and (guess == 'tails' or guess == 'heads'):
        money -= bet
        return "You lost $" + str(bet)
    else:
        return "Type in heads or tails"

#----------------------------------[         cho-han bet       ]----------------------------------
def roll_die(guess, bet):
    global money
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if (dice1+dice2)%2 == 0 and (guess == 'even' or guess == 'odd'):
        money += bet
        return "You won $" + str(bet)
    elif (dice1+dice2)%2 != 0 and (guess == 'even' or guess == 'odd'):
        money -= bet
        return "You lost $" + str(bet)
    else:
        return "Type in even or odd"