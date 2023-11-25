import random
import os

def run():
    IMAGES = [
        '''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
        '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
    ]

    DB = [
        "C",
        "PYTHON",
        "HTML",
        "PHP"
    ]
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attempts = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attempts])
        letter = input("Elige una letra: ").upper()

        found = False
        for idx, char in enumerate(word):
            if char == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts -= 1

        if "_" not in spaces:
            os.system("cls")
            print("Ganaste")
            break

        if attempts == 0:
            os.system("cls")
            print("Perdiste")
            break

if __name__ == "__main__":
    run()
