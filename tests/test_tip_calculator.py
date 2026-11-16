from toolbox.tip_calculator import split_bill


def test_no_tip():
    assert split_bill(100, 0, 4) == 25.0


def test_with_tip():
    assert split_bill(50, 20, 2) == 30.0


def test_rounds_to_cents():
    assert split_bill(10, 0, 3) == 3.33
