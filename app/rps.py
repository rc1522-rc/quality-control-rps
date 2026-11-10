import random

VALID_OPTIONS = ["rock", "paper", "scissors"]


def determine_winner(u, c):
    if u == c:
        return "TIE GAME"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    else:
        return "COMPUTER WINS"


if __name__ == "__main__":

    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in VALID_OPTIONS:
        print("Invalid choice. Please try again.")
        quit()

    computer_choice = random.choice(VALID_OPTIONS)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    result = determine_winner(user_choice, computer_choice)

    print(result)