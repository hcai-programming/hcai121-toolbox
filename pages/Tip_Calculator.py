import streamlit as st
from toolbox.tip_calculator import split_bill

st.title("Tip Calculator")
st.caption("by Eric Pacuit")

total = st.number_input("Bill total ($)", min_value=0.0, value=50.0)
tip = st.slider("Tip (%)", 0, 30, 18)
people = st.number_input("Number of people", min_value=1, value=2)

st.write(f"Each person pays **${split_bill(total, tip, people):.2f}**")
