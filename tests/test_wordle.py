from toolbox.wordle import score, WordleGame


def test_score_all_green():
    assert score("crane", "crane") == [("c", "green"), ("r", "green"), ("a", "green"),
                                       ("n", "green"), ("e", "green")]


def test_score_repeated_letter():
    # only one of the two e's in "geese" is yellow: "crane" has one e, and it is green
    assert score("crane", "geese") == [("g", "gray"), ("e", "gray"), ("e", "gray"),
                                       ("s", "gray"), ("e", "green")]


def test_illegal_guess_is_rejected():
    game = WordleGame(answer="crane")
    assert game.guess("zzzzz") == False
    assert game.history == []


def test_win():
    game = WordleGame(answer="crane")
    game.guess("slate")
    game.guess("CRANE")
    assert game.won()
    assert game.over()


def test_six_wrong_guesses_ends_the_game():
    game = WordleGame(answer="crane")
    for i in range(6):
        game.guess("slate")
    assert not game.won()
    assert game.over()


from toolbox.wordle import play, FilterPlayer, StartWordPlayer, RandomPlayer, legal


def test_filter_player_solves_crane():
    history = play("crane", FilterPlayer("filter"))
    assert history[-1][0] == "crane"
    assert len(history) == 4


def test_start_word_player_opens_with_its_word():
    history = play("crane", StartWordPlayer("slate opener", "slate"))
    assert history[0][0] == "slate"
    assert history[-1][0] == "crane"


def test_random_player_makes_legal_guesses():
    history = play("crane", RandomPlayer("random"))
    assert 1 <= len(history) <= 6
    for guess, feedback in history:
        assert guess in legal
