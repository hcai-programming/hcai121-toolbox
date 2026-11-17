
import streamlit as st
from toolbox.vhuang_functions import get_text_statistics

st.title("Text Statistics")
st.caption("by Vincent Huang")

st.write("Paste your text below to see its statistics.")

text = st.text_area("Enter your text:", height=200)

if st.button("Analyze Text"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        stats = get_text_statistics(text)

        st.subheader("Text Statistics Results")

        st.write(f"**Total Words:** {stats['word_count']}")

        st.write(f"**Longest Word(s):** {', '.join(stats['longest_word'])}")

        st.write(
            f"**Average Word Length:** {stats['average_word_length']} characters"
        )

        st.write(
            f"**Estimated Reading Time (rate of 200 wpm & rounded to 2 decimal places):** {stats['reading_time_minutes']} minutes"
        )

        st.subheader("Most Common Words (Top 5)")

        for word, count in stats["most_common_words"]:
            st.write(f"{word}: {count} times")
