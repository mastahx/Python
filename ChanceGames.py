import random

money = 100

#----------------------------------[         coin flip bet       ]----------------------------------
def flip(guess, bet):
    global money
    coin = random.randint(1,2)
    if money > 0:
        if guess == "heads" or guess == "tails":
            if guess == "heads" and coin == 1:
                money += bet
                return "You won $" + str(bet)
            elif guess == "tails" and coin == 2:
                money += bet
                return "You won $" + str(bet)
            else:
                money -= bet
                return "You lose " + str(bet)
        else:
            return "Type in heads or tails"
    else:
        return "you poor"

#----------------------------------[         cho-han bet       ]----------------------------------
def roll(guess, bet):
    global money
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if money > 0:
        if guess == "even" or guess == "odd":
            if guess == "even" and (dice1 + dice2)%2 == 0:
                money += bet
                return "You won $" + str(bet)
            elif guess == "odd" and (dice1 + dice2)%2 != 0:
                money += bet
                return "You won $" + str(bet)
            else:
                money -= bet
                return "You lose " + str(bet)
        else:
            return "Type in even or odd"
    else:
        return "you poor"

#----------------------------------[         pick card       ]----------------------------------

# while money > 0:
#     print(money)
#     print(flip("heads", 50))