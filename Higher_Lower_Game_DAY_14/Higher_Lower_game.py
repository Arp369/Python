from art import logo
from art import vs
from game_data import data
import random
import os

#Display the art 
print(logo)
score = 0
game_should_continue = True 
account_b = random.choice(data)

while game_should_continue:
    # Generate the random account for game data. 
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    def check_answer(ask_user, a_follower_account, b_follower_account):
        """## Use if statement to check if user is corret or not."""
        if a_follower_account > b_follower_account :
            return ask_user == 'a'
        else:
            return ask_user == 'b'


    #Formate the account data
    account_name1 = account_a ["name"]
    account_desc1 = account_a ["description"]
    account_cont1  = account_a ["country"]
    print (f"Compare A: {account_name1}, {account_desc1}, {account_cont1}")

    print(vs)

    account_name2 = account_b ["name"]
    account_desc2 = account_b ["description"]
    account_cont2  = account_b ["country"]
    print (f"Against B: {account_name2}, {account_desc2}, {account_cont2}")

    # Ask user for a guess 
    ask_user = input("Who has more followers?Type 'A' or 'B': ").lower()
    print (ask_user)

    # Check if user is correct.
    ## Get follower count of each account 
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b ["follower_count"]
    is_correct = check_answer (ask_user, a_follower_account, b_follower_account)

    # Clear the screen between the rounds.
    os.system('cls')

    # Give user feedback on their guess
    # Score keeping 
    if is_correct:
        score += 1
        print(f"You're right! {score}")
        
    else: 
        game_should_continue = False 
        print(f"Sorry, that's wrong. Final Score: {score}") 


# Make the game repeatable.

# Making account of position B become the next account at position A.


      
