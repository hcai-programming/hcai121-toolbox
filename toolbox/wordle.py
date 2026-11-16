"""Wordle, using the code from class (weeks 10 and 11)."""

import random


def load_words(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


answers = load_words("data/answers.txt")         # words that can be the secret word
guesses = load_words("data/valid_guesses.txt")   # every legal guess
legal = set(guesses)


def score(answer, guess):
    """Return a list of (letter, status) pairs, where status is green, yellow, or gray."""
    status = ["gray"] * len(guess)
    remaining = {}
    for i, (g, a) in enumerate(zip(guess, answer)):
        if g == a:
            status[i] = "green"
        else:
            remaining[a] = remaining.get(a, 0) + 1
    for i, (g, a) in enumerate(zip(guess, answer)):
        if status[i] == "gray" and remaining.get(g, 0) > 0:
            status[i] = "yellow"
            remaining[g] = remaining[g] - 1
    return list(zip(guess, status))


# ---------------------------------------------------------------------------
# The players from class
# ---------------------------------------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name

    def new_game(self):
        pass

    def next_guess(self, history):
        return random.choice(guesses)


class RandomPlayer(Player):
    pass


class FilterPlayer(Player):
    def new_game(self):
        self.candidates = list(answers)

    def next_guess(self, history):
        if history:
            last_guess, last_feedback = history[-1]
            self.candidates = [w for w in self.candidates
                               if score(w, last_guess) == last_feedback]
        return self.candidates[0]


class StartWordPlayer(FilterPlayer):
    def __init__(self, name, start_word):
        super().__init__(name)
        self.start_word = start_word

    def next_guess(self, history):
        if not history:
            return self.start_word
        return super().next_guess(history)


def play(answer, player, max_turns=6):
    """Play one game.  Return the history: the list of (guess, feedback) pairs."""
    player.new_game()
    history = []
    for turn in range(1, max_turns + 1):
        guess = player.next_guess(history)
        feedback = score(answer, guess)
        history.append((guess, feedback))
        if guess == answer:
            break
    return history


# ---------------------------------------------------------------------------
# A game played by a person
# ---------------------------------------------------------------------------

class WordleGame:
    def __init__(self, answer=None, max_turns=6):
        if answer is None:
            answer = random.choice(answers)
        self.answer = answer
        self.max_turns = max_turns
        self.history = []          # a list of (guess, feedback) pairs, as in class

    def guess(self, word):
        """Add a guess to the history.  Return False if the word is not a legal guess."""
        word = word.strip().lower()
        if word not in legal:
            return False
        self.history.append((word, score(self.answer, word)))
        return True

    def won(self):
        return len(self.history) > 0 and self.history[-1][0] == self.answer

    def over(self):
        return self.won() or len(self.history) >= self.max_turns
