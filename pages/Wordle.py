import streamlit as st
from toolbox.wordle import WordleGame

st.title("Wordle")
st.caption("by Eric Pacuit")

BOXES = {"green": "🟩", "yellow": "🟨", "gray": "⬜"}

# Streamlit reruns this whole file after every click, so the game object
# is kept in st.session_state, which survives the reruns.
if "wordle_game" not in st.session_state:
    st.session_state["wordle_game"] = WordleGame()
game = st.session_state["wordle_game"]

if not game.over():
    word = st.text_input("Your guess (a 5-letter word)", max_chars=5)
    if st.button("Guess"):
        if not game.guess(word):
            st.error(f"'{word}' is not in the word list.")

for guess, feedback in game.history:
    st.write("  ".join(BOXES[status] + " " + letter.upper() for letter, status in feedback))

if game.won():
    st.success(f"You got it in {len(game.history)} guesses!")
elif game.over():
    st.error(f"Out of guesses. The word was {game.answer.upper()}.")

if st.button("New game"):
    st.session_state["wordle_game"] = WordleGame()
    st.rerun()
