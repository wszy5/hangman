import random
import wikipediaapi as wiki

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

with open("animals.txt","r") as file:
  word_list = [i.strip() for i in file.readlines()]

wiki_instance = wiki.Wikipedia("en")
phrase = random.choice(word_list).lower()

page = wiki_instance.page(phrase).summary.lower()

res = page[page.index(phrase)+len(phrase):page.index(".")]


d = 0

display = ["_" for i in range(len(phrase))]

while True:
    if "".join(display) == phrase:
      print("\n\nYou win!")
      break  
    print(res)

    guess = (input("\nGuess a letter: ")).lower()
    while guess.isalpha() == False:
      guess = (input("\nGuess a letter: ")).lower()
  
    if guess in phrase:
        for i in range(len(phrase)):
          letter = phrase[i]
          if letter == guess:
            display[i] = letter
          
        print("\nRIGHT\n")
        print(*display)
    else:
        print("\nBAD\n")
        d+=1
        if d==6:
            print(HANGMANPICS[d])
            print(f"\n\nYou lose! The phrase: {phrase}")
            break
        print(HANGMANPICS[d])