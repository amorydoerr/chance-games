import random


def perform_win(bet: int) -> int:
    win = int(bet * 2)
    print(f"You won {win}!")
    return win


def perform_loss(bet: int) -> int:
    loss = int(bet * -1)
    print(f"You lost {loss * -1}...")
    return loss


def perform_tie() -> int:
    print(f"You tied.")
    return 0


def coin_flip(bet: int, guess: str) -> int:
    flip = random.choice(["heads", "tails"])
    print(f"The coin landed on: {flip}")
    if flip == guess:
        return perform_win(bet)
    else:
        return perform_loss(bet)


def cho_han(bet: int, guess: str) -> int:
    roll = random.randint(1, 6)
    print(f"The roll was: {roll}")
    if guess == "odd" and roll % 2 == 1 or guess == "even" and roll % 2 == 0:
        return perform_win(bet)
    else:
        return perform_loss(bet)


def war(bet: int) -> int:
    deck_conversions = {  # number values for named cards
        1: "ace",
        11: "jack",
        12: "queen",
        13: "king"
    }
    deck = list(range(1, 14)) * 4
    draw_player = random.choice(deck)
    deck.remove(draw_player)
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
    if choice == "00":
        choice = -1
    if choice == "0":
        choice = int(choice)
    red = (1, 3, 5, 7, 9, 12,
           14, 16, 18, 19, 21, 23,
           25, 27, 30, 32, 34, 36)
    black = (2, 4, 6, 8, 10, 11,
             13, 15, 17, 20, 22, 24,
             26, 28, 29, 31, 33, 35)
    special = {-1: "00"}
    roll = random.choice(range(-1, 37))
    print(f"The roulette rolled: {special.get(roll, roll)}")
    if roll > 0 and type(choice) is str:  # not 0/00
        if choice == "even" and roll % 2 == 0 or choice == "odd" and roll % 2 == 1 or choice == "black" and roll in black or choice == "red" and roll in red:
            return perform_win(bet / 2)  # payout 2:1

    if choice == roll:  # 0/00
        return perform_win(bet * 35/2)  # payout 35:1

    return perform_loss(bet)
