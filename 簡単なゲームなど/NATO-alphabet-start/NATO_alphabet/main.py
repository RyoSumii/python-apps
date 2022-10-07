import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}

input_word = input("Enter a word: ").upper()
nato_list = [nato[letter] for letter in input_word]

print(nato_list)
