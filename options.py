from games import coin_flip, cho_han, war, roulette
from os import system

game_options = {
    1: coin_flip,
    2: cho_han,
    3: war,
    4: roulette,
    'Q': None,
    'R': None
}

menu = """Choose a game:
1. Coin Flip
2. Chō-han
3. War
4. Roulette
R. Rules
Q. Quit
"""

rules = """
Coin Flip: Choose heads or tails
Chō-han: Guess if a dice roll will be odd or even
War: Draw a card with the cpu, higher card wins
Roulette: Choose black, red to double your bet or 0/00 to multiply by 35
"""
bar_line = "-------------------------"

class MoneyError(Exception):
    pass


class ChoiceError(Exception):
    pass


def validate_game_input(money):
    try:
        player_choice = input(menu).upper()
        if player_choice == 'R':
            system("cls")
            print(rules)
            return False, True, None, None
        if player_choice == 'Q':
            system("cls")
            return True, False, None, None  # sets playing to False
        player_choice = int(player_choice)
        if player_choice not in game_options:
            raise ValueError
        valid_input = False
        system("cls")
        while not valid_input:
            valid_input, player_bet = validate_bet_input(money)
        return True, True, player_choice, player_bet
    except ValueError:
        system("cls")
        print("Please chooose a valid option")
        print(bar_line)
        return False, True, None, None


def validate_bet_input(money):
    print(f"Remaining money: {money}")
    try:
        player_bet = int(input("Enter a bet: "))
        if player_bet <= 0:
            raise ValueError
        if player_bet > money:
            raise MoneyError
        return True, player_bet
    except MoneyError:
        system("cls")
        print("You don't have enough money!")
        print(bar_line)
        return False, None
    except ValueError:
        system("cls")
        print("Please enter a valid bet")
        print(bar_line)
        return False, None


def validate_argument_input(player_choice):
    game_argument = None
    if player_choice == 1:
        try:
            valid_inputs = ("heads", "tails")
            game_argument = input("Heads or tails? ").lower()
            if game_argument not in valid_inputs:
                raise ChoiceError
        except ChoiceError:
            system("cls")
            print('Please type "heads" or "tails"')
            print(bar_line)
            return False, None
    if player_choice == 2:
        try:
            valid_inputs = ("odd", "even")
            game_argument = input("Odd or even? ").lower()
            if game_argument not in valid_inputs:
                raise ChoiceError
        except ChoiceError:
            system("cls")
            print('Please type "odd" or "even"')
            print(bar_line)
            return False, None
    if player_choice == 4:
        try:
            valid_inputs = ("red", "black", "0", "00")
            game_argument = input(
                "Red, black, 0, or 00? ").lower()
            if game_argument not in valid_inputs:
                raise ChoiceError
        except ChoiceError:
            system("cls")
            print('Please type "red", "black", "0", or "00"')
            print(bar_line)
            return False, None
    system("cls")
    return True, game_argument


def start_game():
    print("Welcome to Games of Chance!")
    input("Press enter to start")
    system("cls")


def end_game(money):
    if money > 0:
        print(f"Final money: {money}")
        print("Thanks for playing!")
    else:
        print("You lost it all!")
        print("Better luck next time...")

def restart_game():
    try:
        restart = input("Would you like to play again? (Y/N)\n").upper()
        if restart == 'Y':
            return True, True
        if restart == 'N':
            return True, False
        raise ValueError
    except ValueError:
        system("cls")
        print('Please choose "Y" or "N"')
        return False, None