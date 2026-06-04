import streamlit as st
import os

st.title("🎵 AI Music Generator")
st.audio("generated_music.wav")
st.write("Generate AI music using LSTM model trained on MIDI data")

if st.button("🎼 Generate Music"):
    st.write("Generating music... please wait")

    with st.spinner("Creating music..."):
        os.system("python generate.py")

    st.success("Music generated!")

    st.audio("generated_music.wav")