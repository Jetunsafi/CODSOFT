import random

opt = ["Rock", "Paper", "Scissors"]
print("\nWELCOME TO ROCK,PAPER,SCISSORS GAME")
print("____________________________________")

while True:
    user = input("Choose Rock, Paper, Scissors (or Exit):").capitalize()

    if user == "Exit":
        print("Thanks for playing!")
        break

    comp = random.choice(opt)
    print("Computer chose:", comp)

    if user == comp:
        print("Its a Tie!")

    elif(user == "Rock" and comp == "Scissors") or (user == "Scissors" and comp == "Paper") or (user == "Paper" and comp == "Rock"):
        print("You win!")

    else:
        print("Computer wins!")
