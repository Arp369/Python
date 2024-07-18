# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  print("What is your name?: ")
  name = input()
  print("What is your bid?: $")
  price = int(input())
  bids[name] = price
  print("Are there any other bidders? Type 'yes' or 'no'.")
  should_continue = input()
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  # elif should_continue == "yes":
  #   clear()
