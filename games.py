import random


def perform_win(bet: int) -> int:
    """ Prints win message and returns winning amount. """

    win = int(bet * 2)
    print(f"You won {win}!")
    return win


def perform_loss(bet: int) -> int:
    """ Prints loss message and returns losing amount. """

    loss = int(bet * -1)
    print(f"You lost {loss * -1}...")
    return loss


def perform_tie() -> int:
    """ Prints tie message and returns 0. """

    print(f"You tied.")
    return 0


def coin_flip(bet: int, guess: str) -> int:
    """ Simulates a coin flip game.

    Compares a simulation of a coin flip to a player guess and
    performs a win or loss accordingly.

    Args:
        bet: Player bet amount.
        guess: Player guess ('heads' or 'tails').

    Returns:
        Amount of money won or lost depending on bet.
    """

    flip = random.choice(["heads", "tails"])
    print(f"The coin landed on: {flip}")
    if flip == guess:
        return perform_win(bet)
    else:
        return perform_loss(bet)


def cho_han(bet: int, guess: str) -> int:
    """ Simulates a Chō-han game.

    Compares the parity of a 6-sided dice roll to a user
    guess and performs a win or loss accordingly.

    Args:
        bet: Player bet amount.
        guess: Player guess ('odd' or 'even').

    Returns:
        Amount of money won or lost depending on bet.
    """

    roll = random.randint(1, 6)
    print(f"The roll was: {roll}")
    if guess == "odd" and roll % 2 == 1 or guess == "even" and roll % 2 == 0:
        return perform_win(bet)
    else:
        return perform_loss(bet)


def war(bet: int) -> int:
    """ Simulates a round of the card game war.

    Compares cpu and player draw from a 52 card deck and performs a win,
    loss, or tie accordingly. The winning card is that of a higher value.

    Args:
        bet: Player bet amount.

    Returns:
        Amount of money won or lost depending on bet.
    """

    deck_conversions = {  # number values for named cards
        1: "ace",
        11: "jack",
        12: "queen",
        13: "king"
    }
    deck = list(range(1, 14)) * 4
    draw_player = random.choice(deck)
    deck.remove(draw_player)  # removes draw from deck
    print(f"You drew: {deck_conversions.get(draw_player, draw_player)}")
    draw_cpu = random.choice(deck)
    print(f"Cpu drew: {deck_conversions.get(draw_cpu, draw_cpu)}")
    if draw_player > draw_cpu:
        return perform_win(bet)
    elif draw_player < draw_cpu:
        return perform_loss(bet)
    else:
        return perform_tie()


def roulette(bet: int, choice: str) -> int:
    """  Simulates a round of roulette.

    Simulates a roll of a roulette table and performs a win or loss
    depending on the players choice.

    Args:
        bet: Player bet amount.
        choice: Player choice ('0', '00', 'odd', 'even', red', or 'black').

    Returns:
        Amount of money won or lost accordingly.
    """

    red = (1, 3, 5, 7, 9, 12,
           14, 16, 18, 19, 21, 23,
           25, 27, 30, 32, 34, 36)
    black = (2, 4, 6, 8, 10, 11,
             13, 15, 17, 20, 22, 24,
             26, 28, 29, 31, 33, 35)
    # convert str choices to appropriate int values
    if choice == "00":
        choice = -1
    if choice == "0":
        choice = int(choice)
    roll = random.choice(range(-1, 37))  # roll one of 38 integers
    print(f"The roulette rolled: {special.get(roll, roll)}")
    # 0 and 00 not included in odd or even options
    if roll > 0 and type(choice) is str:
        if choice == "even" and roll % 2 == 0 or choice == "odd" and roll % 2 == 1 or choice == "black" and roll in black or choice == "red" and roll in red:
            return perform_win(bet / 2)  # payout 1:1
    else if choice == roll:
        return perform_win(bet * 35/2)  # payout 35:1
    return perform_loss(bet)
