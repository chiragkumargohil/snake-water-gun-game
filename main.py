# Game: Snake - Water - Gun

import random

def game(a, b):
    if a == b:
        return None
    elif a == "s":
        if b == "w":
            return False
        elif b == "g":
            return True
    elif a == "w":
        if b == "g":
            return False
        elif b == "s":
            return True
    elif a == "g":
        if b == "s":
            return False
        elif b == "w":
            return True

print("Welcome to the Snake Water Gun Game. Let's understand the rules:\n1. Snake vs. Water: Snake drinks the water hence wins.\n2. Water vs. Gun: The gun will drown in water, hence a point for water.\n3. Gun vs. Snake: Gun will kill the snake and win.\n4. In situations where both players choose the same object, the result will be a draw. So, let's start...\n")

compScore = 0
yourScore = 0
matchPlayed = 0
while True:
    # start - inputs from computer and user

    comp = print("Computer's Turn...")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = "s"
    elif randNo == 2:
        comp = "w"
    elif randNo == 3:
        comp = "g"

    player = input("Your Turn: Snake (s) / Water (w) / Gun (g) (write 'over' to quit the game): ")
    if player == "s" or player == "w" or player == "g":
        pass
    elif player == "over":
        print(f"\nFinal Score is {compScore} - {yourScore}\nTotal Matches Played {matchPlayed}.")
        if yourScore > compScore:
            print("Congratulations! You won the battle.\nThank you for Playing.")
        elif compScore > yourScore:
            print("Better luck next time. You lost the battle.\nThank you for Playing.")
        else:
            print("Match Drawn.\nThank you for Playing.")
        exit()
    else:
        print("Invalid input. Try again...\n")
        continue

    # end - inputs from computer and user

    print(f"\nComputer = {comp} || You = {player}")
    
    result = game(comp, player)
    if result == None:
        print(f"\nMatch Tie.")
    elif result:
        print("\nYou Win")
        yourScore = yourScore + 1
    else:
        print("\nYou Loose")
        compScore = compScore + 1
    print(f"\nScore is {compScore} - {yourScore}\n")
    matchPlayed = matchPlayed + 1
