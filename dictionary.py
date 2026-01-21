import streamlit as st

# Dictionary data
dictionary = {
    "hello": "hola",
    "goodbye": "adiós",
    "please": "por favor",
    "thank you": "gracias",
    "yes": "sí",
    "no": "no",
    "man": "hombre",
    "woman": "mujer",
    "boy": "niño",
    "girl": "niña",
    "food": "comida",
    "water": "agua",
    "house": "casa",
    "school": "escuela",
    "book": "libro",
    "friend": "amigo",
    "family": "familia",
    "love": "amor",
    "work": "trabajo",
    "money": "dinero",
    "time": "tiempo"
}

# App title
st.title("English to Spanish Dictionary")

# Instruction
st.write("Enter an English word to see its Spanish meaning")

# Text input
word = st.text_input("Enter an English word:")

# Button
if st.button("Translate"):
    if word.lower() in dictionary:
        st.success(f"Spanish meaning: {dictionary[word.lower()]}")
    else:
        st.error("Word not found in dictionary")
