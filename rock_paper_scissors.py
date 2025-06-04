import random

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user == 'exit':
        break
    if user not in options:
        print("Invalid choice!")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")
