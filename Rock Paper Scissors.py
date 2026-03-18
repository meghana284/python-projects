import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Game Over")
        break
