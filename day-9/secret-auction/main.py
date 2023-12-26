import os
from art import logo

# for visualize the programe we can use pythontutor
# https://pythontutor.com/


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ''
    for key, value in bidders.items():
        bid_amount = bidders[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bidders=bids)
    elif should_continue == 'yes':
        clear_terminal()
