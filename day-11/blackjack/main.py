##### Blackjack House Rules #####
# Deck is unlimited in size
# There are no jokers
# Jack/King/Queen all count as 10
# The ACE can count as 11 or 1
# use the following list as the deck of cards:
import random


def clear_terminal():
    print("\033c", end="")


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# create function called calculate_score() that takes a list of cards as input and returns a score
def calculate_score(cards):
    """Take a list of cards and return the calculated score from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). if the score is already 21 remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# create a function called compare and pass in the user_score and computer score. If the user and computer both have the same score, then it's draw. If the computer has a blackjack (0), then user loses. If the user has blackjack then users wins. if the user_score is over 21, then the user loses. if the computer score is over 21 then the computer loses. If none of above the the player with the highest score wins.


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has blackjack!"
    elif user_score == 0:
        return "Win with a blackjack!"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Opponent went over. You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You lose."


continue_play = False
while not continue_play:
    # deal user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # call calculate_score(). If the computer or user has a blackjack(0) or if the user score is over 21, then game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # ask the user if they want to restart the game. if the answer is yes, clear console and start a new game if blackjack
    play = input(
        "Do you want to play a game of blackjack? Type 'y' or 'n': ")

    if play == "n":
        continue_play = True
    else:
        clear_terminal()
