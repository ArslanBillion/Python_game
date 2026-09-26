import random
computer  = random.choice([-1,0,1])
youstr = input("enter your choice :")
youDict ={"s": 1, "w":-1,"g":0}
reverseDict ={1: "snake", -1: "water", 0:"gun"}
you = youDict[youstr]
#by now we have 2 numbers (variables),you and computer

print(f"you chose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")
if(computer==you):
    print("its a draw @")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("You lose!")
    else:
        print("You win!")