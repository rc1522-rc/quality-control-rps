import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ").lower()

if user_choice not in VALID_OPTIONS:
    print("Invalid choice. Please try again.")
    quit()

computer_choice = random.choice(VALID_OPTIONS)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("TIE GAME")
elif user_choice == "rock" and computer_choice == "scissors":
    print("USER WINS")
elif user_choice == "paper" and computer_choice == "rock":
    print("COMPUTER WINS")
elif user_choice == "scissors" and computer_choice == "paper":
    print("USER WINS")
else:
    print("COMPUTER WINS")