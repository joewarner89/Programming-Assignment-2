
from art1 import logo, vs
from game_data import data
import random

# format account data into printable format

def get_random_account():
    """

    :return: Get the data from random account
    """
    return random.choice(data)


def format_account(account):
    """
    :param account: Takes acount a and be
    :return: format name descriptions and coutry into printable format
    """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_desc}, from {account_country}"

def check_answer(guess,a_followers, b_followers):
    """

    :param guess: parameters to initiate who has more followers between A and B
    :param a_followers: the number counts for A followers
    :param b_followers: the number of counts for B followers
    :return: if the statements checks the users is correct
    """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
# Display the art
# make the game repeatable
def game():
    print(logo)
    score = 0
    game_should_continue = True
    # generate random number for the account_a and account_b
    account_a = get_random_account()
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        acoount_b = get_random_account()

        while account_a == acoount_b:
            account_b = get_random_account()
        print(f'Compare A: {format_account(account_a)}.')
        print(vs)
        print(f'Compare B :  {format_account(account_b)}')

        # Ask a user for a guess
        guess = input("Who has more followers? Type 'A' or 'B' ").lower()
        # Generate a ramdom account from the data
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        # use if statements to check if user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)


        # Check if user is correct and print the answer and the score
        if is_correct:
            score += 1
            print(f'You are right! Current score is {score}')
        else:
            print(f'Sorry!, You are wrong! Final score is {score}')







game()



