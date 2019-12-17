import random

p = 0
c = 0
list1 = ['s','w','g']
print("Welcome to Snake,Water & Gun Game!")
print("Press s for Snake")
print("Press w for Water")
print("Press g for Gun")
print("any other input apart from s,w,g are invalid")
print("\n")
n = str(input("Enter your Name:"))

for i in range(15):

    computer = random.choice(list1)

    print("Enter your choice")
    player = str(input())

    if computer == 'w' and player == list1[0]:
        print("Computer:", computer)
        print(n, "wins")
        p += 1
    elif computer == 'w' and player == list1[2]:
        print("Computer:", computer)
        print("computer wins")
        c += 1

    elif computer == 's' and player == list1[1]:
        print("Computer:", computer)
        print("computer wins")
        c += 1
    elif computer == 's' and player == list1[2]:
        print("Computer:", computer)
        print(n, "wins")
        p += 1
    elif computer == 'g' and player == list1[1]:
        print("Computer:", computer)
        print(n, "wins")
        p += 1
    elif computer == 'g' and player == list1[0]:
        print("Computer:", computer)
        print("computer wins")
        c += 1
    elif player == computer:
        print("Computer:", computer)
        print("Draw")
    else:
        print("Invalid Input by", n)
print("\n")
if c == p:
    print("Computer score:", c, "Your score: ", p)
    print(" Result: The score is draw")
else:
    if c > p:
        print("Computer score: ", c, "Your score: ", p)
        print("Result: Computer wins. Better Luck next time")
    else:
        print("Computer score: ", c, "Your score: ", p)
        print("Result: Congratulations", n, "You've beat the computer")

