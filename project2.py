#Rock,Paper amd Scissors Game
import random
choose=['rock','paper','scissors']
computer=random.choice(choose)
player=input("rock, paper or scissors?").lower()
if player==computer:
    print("Tie")
elif player=='rock':
    if computer=='paper':
        print("You lose!",computer,"covers",player)
    else:
        print("You win!",player,"smashes",computer)
elif player=='paper':
    if computer=='scissors':
        print("You lose!",computer,"cut",player)
    else:
        print("You win!",player,"covers",computer)
elif player=='scissors':
    if computer=='rock':
        print("You lose!",computer,"smashes",player)
    else:
        print("You win!",player,"cut",computer)
else:
    print("Invalid input! You lose!")
print("Thanks for playing")