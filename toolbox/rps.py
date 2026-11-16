"""Rock, paper, scissors, using the code from Project 1."""

import random


def random_move():
    n = random.randint(1, 3)
    if n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"


def winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"


def beat(move):
    if move == "rock":
        return "paper"
    elif move == "paper":
        return "scissors"
    else:
        return "rock"


def score(player, computer):
    result = winner(player, computer)
    if result == "player":
        return 1
    elif result == "computer":
        return -1
    else:
        return 0


# ---------- strategies ----------
# A strategy takes the round number and the other side's last move, and returns
# "rock", "paper", or "scissors".  The last move is None in round 1.


def always_rock(round_number, last_computer_move):
    return "rock"


def play_random(round_number, last_computer_move):
    return random_move()


def cycle(round_number, last_computer_move):
    # Plays rock, scissors, paper, in order, then repeats.
    leftover = round_number % 3
    if leftover == 1:
        return "rock"
    elif leftover == 2:
        return "scissors"
    else:
        return "paper"


def beat_last(round_number, last_computer_move):
    if last_computer_move is None:
        return "rock"
    else:
        return beat(last_computer_move)


class RPSMatch:
    """A match between a person and a computer that uses one of the strategies.

    Like play_rounds from Project 1, but one round at a time.
    """

    def __init__(self, opponent=play_random):
        self.opponent = opponent
        self.round_number = 0
        self.last_player = None
        self.total = 0

    def play_round(self, player):
        """Play one round.  Return the computer's move and the winner."""
        self.round_number = self.round_number + 1
        computer = self.opponent(self.round_number, self.last_player)
        self.total = self.total + score(player, computer)
        self.last_player = player
        return computer, winner(player, computer)
