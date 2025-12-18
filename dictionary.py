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

print("English to Spanish Dictionary")
print("Type 'exit' to quit\n")

while True:
    word = input("Enter an English word: ").lower()

    if word == "exit":
        print("Goodbye!")
        break

    if word in dictionary:
        print(f"Spanish meaning: {dictionary[word]}\n")
    else:
        print("Word not found in dictionary.\n")
