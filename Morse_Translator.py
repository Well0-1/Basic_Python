MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "Ç": "-.-..",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "Ö": "---.",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "Ü": "..--",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def decode():
    encoded_text = input("Enter the Morse Code: ").split(" ")
    decoded = ""

    for i in range(len(encoded_text)):
        if encoded_text[i] == "/":
            decoded += " "
        for t, m in MORSE_CODE_DICT.items():
            if encoded_text[i] == m:
                decoded += t

    print(decoded)


def encode():
    text_to_morse = input("Enter the text you want to convert to Morse Code: ").upper()
    encoded = ""

    for i in range(len(text_to_morse)):
        if text_to_morse[i] == " ":
            encoded += "/ "
        for t, m in MORSE_CODE_DICT.items():
            if text_to_morse[i] == t:
                encoded += m + " "

    print(encoded)


while True:
    action = input("1.Text-to-Morse\n2.Morse-to-Text\nEnter Your Choice: ")
    if action == "1":
        encode()
        break
    elif action == "2":
        decode()
        break
    else:
        print("Invalid Action Shutting Down...")
        quit()
