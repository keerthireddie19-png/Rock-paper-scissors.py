import random

choices = ["rock", "paper", "scissors"]

user = input("enter rock, paper or scissors:")
computer = random.choice(choices)

print("user choice:", user)
print("computer choice:", computer)

if user == computer:
    print("it's a tie!")

elif (user == "rock"and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("you win!")

else:
    print("computer wins!")