import random as rd
print("__________________________DICE ROLLING GAME____________________")

while(True):
    dice = input("Roll the Dice(Y/N) : ")
    if dice == "y" or dice == "Y":
        die1 = rd.randint(1,6)
        die2 = rd.randint(1,6)
        print(f"({die1} ,{die2})")
    elif dice == "n" or dice == "N":
        print("Tnaks for playing!")
        break
    else :
        print("Invalid choice")
