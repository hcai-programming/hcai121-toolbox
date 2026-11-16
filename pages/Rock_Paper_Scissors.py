import streamlit as st
from toolbox.rps import RPSMatch, play_random, always_rock, cycle, beat_last

st.title("Rock, Paper, Scissors")
st.caption("by Eric Pacuit")

STRATEGIES = {"random": play_random, "always rock": always_rock,
              "cycle": cycle, "beat your last move": beat_last}

choice = st.selectbox("Play against", list(STRATEGIES))

# A new match starts whenever you pick a different opponent.
if "rps_match" not in st.session_state or st.session_state["rps_opponent"] != choice:
    st.session_state["rps_match"] = RPSMatch(STRATEGIES[choice])
    st.session_state["rps_opponent"] = choice
match = st.session_state["rps_match"]

columns = st.columns(3)
for column, move in zip(columns, ["rock", "paper", "scissors"]):
    if column.button(move):
        computer, result = match.play_round(move)
        st.write(f"You chose **{move}**, the computer chose **{computer}**.")
        if result == "tie":
            st.write("It's a tie!")
        elif result == "player":
            st.write("You win!")
        else:
            st.write("Computer wins!")

st.write(f"Round {match.round_number}, your score: **{match.total}**")
