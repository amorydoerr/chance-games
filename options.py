""" Contains functions to perform technical flow of program. """

from os import system
from typing import Tuple
from games import coin_flip, cho_han, war, roulette

# conversion of user selection to appropriate function
GAME_OPTIONS = {
    1: coin_flip,
    2: cho_han,
    3: war,
    4: roulette
}
# printable menu with options
MENU = """Choose a game:
1. Coin Flip
2. Chō-han
3. War
4. Roulette
R. Rules
Q. Quit
"""
# printable ruleset for games
RULES = """
Coin Flip: Choose heads or tails
Chō-han: Guess if a dice roll will be odd or even
War: Draw a card with the cpu, higher card wins
Roulette: Choose black, red to double your bet or 0/00 to multiply by 35
"""
# dashed divider to aid visibility
BAR_LINE = "-------------------------"

class MoneyError(Exception):
    """ Custom exception for validate_bet_input(). """


class ChoiceError(Exception):
    """ Custom exception for validate_game_input(). """


def validate_game_input(money: int) -> Tuple[bool, bool, int, int]:
    """ Ensures appropriate input during menu selection.

    Performs tests on user input to ensure valid entries. Return values allow
    continuous looping of the function until valid input is recieved.

    Args:
        money: current amount of user money used for validate_bet_input().

    Returns:
        Values for valid_input, playing, player_choice, player_bet in main.
        A value for valid_input of True signifies successful player input.
        A value for playing of False allows the initiation of the end-game sequence.
        Values for player_choice and player_bet depend on input recieved.
    """

    try:
        player_choice = input(MENU).upper()
        if player_choice == 'R':
            system("cls")
            print(RULES)
            return False, True, None, None
        if player_choice == 'Q':
            system("cls")
            return True, False, None, None  # sets playing to False
        player_choice = int(player_choice)
        if player_choice not in GAME_OPTIONS:
            raise ValueError
        valid_input = False
        system("cls")
        while not valid_input:
            valid_input, player_bet = validate_bet_input(money)
        return True, True, player_choice, player_bet
    except ValueError:
        system("cls")
        print("Please chooose a valid option")
        print(BAR_LINE)
        return False, True, None, None


def validate_bet_input(money) -> Tuple[bool, int]:
    """ Ensures appropriate input during bet amount selection.

    Performs tests on user input to ensure valid entries. Return values
    allow for continuous looping of the function until valid input is recieved.

    Args:
        money: current amount of user money.

    Returns:
        Values for valid_input, player_bet in validate_game_input().
        A value for valid_input of True signifies successful player input.
        The value for player_bet depends on input recieved.
    """

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
        print(BAR_LINE)
        return False, None
    except ValueError:
        system("cls")
        print("Please enter a valid bet")
        print(BAR_LINE)
        return False, None


def validate_argument_input(player_choice: int) -> Tuple[bool, str]:
    """ Ensures appropriate input during gameplay.

    Performs on tests for user input depending on the game chosen. Each
    game option has specific values to be chosen from. Return values allow for
    continuous looping of the function until valid input is recieved.

    Args:
        player_choice: input recieved corresponding to a game

    Returns:
        Values for valid_input, game_argument to main.py.
        A value for valid_input of True signifies successful player input.
        Value for game_argument depends on player input.
    """

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
            print(BAR_LINE)
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
            print(BAR_LINE)
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
            print(BAR_LINE)
            return False, None
    system("cls")
    return True, game_argument


def start_game() -> None:
    """ Prints welcome message and pauses until enter is presses. """

    print("Welcome to Games of Chance!")
    input("Press enter to start")
    system("cls")


def end_game(money) -> None:
    """ Prints amount of money remaining at end of game. """

    if money > 0:
        print(f"Final money: {money}")
        print("Thanks for playing!")
    else:
        print("You lost it all!")
        print("Better luck next time...")

def restart_game() -> Tuple[bool, bool]:
    """ Validates player input to determine whether to restart or exit.

    Returns:
        values for valid_input and restart to main().
        A value for valid_input of True signifies successful player input.
        Value for restart depends on player input.
    """

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
