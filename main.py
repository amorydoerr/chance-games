from options import validate_game_input, validate_bet_input, validate_argument_input, start_game, end_game, restart_game, bar_line, game_options
from os import system
import sys


def main():
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
            money += game_options[player_choice](player_bet, game_argument)
        else:
            money += game_options[player_choice](player_bet)
        print(bar_line)
    end_game(money)
    valid_input = False
    while not valid_input:
        valid_input, restart = restart_game()
    if restart:
        main()
    sys.exit()


if __name__ == "__main__":
    main()
