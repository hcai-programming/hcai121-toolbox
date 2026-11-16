from toolbox.rps import winner, beat, score, always_rock, beat_last, RPSMatch


def test_winner():
    assert winner("rock", "scissors") == "player"
    assert winner("rock", "paper") == "computer"
    assert winner("rock", "rock") == "tie"


def test_beat():
    assert winner(beat("rock"), "rock") == "player"
    assert winner(beat("paper"), "paper") == "player"
    assert winner(beat("scissors"), "scissors") == "player"


def test_match_against_always_rock():
    match = RPSMatch(always_rock)
    assert match.play_round("paper") == ("rock", "player")
    assert match.play_round("scissors") == ("rock", "computer")
    assert match.round_number == 2
    assert match.total == 0


def test_beat_last_uses_your_last_move():
    match = RPSMatch(beat_last)
    match.play_round("scissors")
    computer, result = match.play_round("scissors")
    assert computer == "rock"
    assert result == "computer"
