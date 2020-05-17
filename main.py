""" Main game driver. """

from os import system
from options import validate_game_input, validate_argument_input, start_game
from options import end_game, restart_game, BAR_LINE, GAME_OPTIONS


def main():
    """ Runs game functions """

    system("cls")
    playing = True
    money = 100
    start_game()
    while money > 0:
        valid_input = False
        while not valid_input:
            valid_input, playing, player_choice, player_bet = validate_game_input(
                money)
        if not playing:
            break
        game_argument = None
        valid_input = False
        while not valid_input:
            valid_input, game_argument = validate_argument_input(player_choice)
        if game_argument is not None:
            money += GAME_OPTIONS[player_choice](player_bet, game_argument)
        else:
            money += GAME_OPTIONS[player_choice](player_bet)
        print(BAR_LINE)
    end_game(money)
    valid_input = False
    while not valid_input:
        valid_input, restart = restart_game()
    if restart:
        main()
    else:  # Prevent unnecesary command line clears
        system("cls")


if __name__ == "__main__":
    main()
