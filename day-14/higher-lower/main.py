from random import choice
from art import logo, vs
from game_data import data


def clear_terminal():
    print("\033c", end="")


def format_data(account):
    """Take the accounts data and returns the printable format."""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
should_continue = True
account_b = choice(data)

while should_continue:
    # Generate a random account from the game data

    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    # Format the account data into printable format.
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get followers count of each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear_terminal()
    print(logo)
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're Right! Current score: {score}")
    else:
        should_continue = False
        print(f"Sorry! that's wrong. Final score: {score}")
