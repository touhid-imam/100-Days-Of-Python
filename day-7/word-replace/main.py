import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# step - 1
word_list = ["Adventure", "Baboon", "Camel"]
random.shuffle(word_list)
# Todo-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

# print(randWord)
# Todo-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = 0

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Todo - 3 Check if the letter the user guessed (guess) is one of the letters in the choosen word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")
