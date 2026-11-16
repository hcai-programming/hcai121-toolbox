def split_bill(total, tip_percent, people):
    """Return how much each person pays, rounded to cents."""
    with_tip = total * (1 + tip_percent / 100)
    return round(with_tip / people, 2)
