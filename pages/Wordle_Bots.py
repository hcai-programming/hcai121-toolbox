import streamlit as st
from toolbox.wordle import answers, play, RandomPlayer, FilterPlayer, StartWordPlayer

st.title("Wordle Bots")
st.caption("by Eric Pacuit")
st.write("Pick a secret word and a bot, and watch the bot play.")

BOXES = {"green": "🟩", "yellow": "🟨", "gray": "⬜"}

BOTS = {"filter": FilterPlayer("filter"),
        "slate opener": StartWordPlayer("slate opener", "slate"),
        "random": RandomPlayer("random")}

words = sorted(answers)
secret = st.selectbox("Secret word", words, index=words.index("crane"))
bot_name = st.selectbox("Bot", list(BOTS))

if st.button("Play"):
    history = play(secret, BOTS[bot_name])
    for guess, feedback in history:
        st.write("  ".join(BOXES[status] + " " + letter.upper() for letter, status in feedback))
    if history[-1][0] == secret:
        st.success(f"{bot_name} solved it in {len(history)} guesses.")
    else:
        st.error(f"{bot_name} did not solve it in 6 guesses.")
