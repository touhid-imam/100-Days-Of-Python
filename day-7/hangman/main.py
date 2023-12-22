import random
from hangman_words import word_list
from art import stages, logo

# step - 1
word_list = ["Adventure", "Baboon", "Camel"]
random.shuffle(word_list)
# Todo-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

end_of_game = 0
lives = 6

# Logo
print(logo)
# Notification to Gamer user
print(f"Psst, the solution is {chosen_word}")
# print(randWord)
# Todo-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # a letter which already gussed
    if guess in display:
        print(f"You've already guessed {guess}")
    # Todo - 3 Check if the letter the user guessed (guess) is one of the letters in the choosen word.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You Guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(stages[lives])
