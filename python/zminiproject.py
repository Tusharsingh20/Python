#  1 for snake
#  -1 for water
#  0 for gun
import random

computer = random.choice([-1,0,1])
youstr = input("Enter the value:- ")
youdict ={ "q" : 1 ,"w":-1,"e":0}
reversedict={1: "snake",-1:"water",0: "gun"}
you=youdict[youstr]

print(f" computer choice the {reversedict[computer]} \n you choice it { reversedict[you]}")
if(computer==you):
    print("Its A Draw")

else:
    if(computer== -1 and you ==1):
        print("You are win")
    elif(computer== -1 and you ==0):
        print("You are Lose")
    elif(computer== 1 and you ==-1):
        print("You are Lose")
    elif(computer== 1 and you ==0):
        print("You are win")
    elif(computer== 0 and you ==1):
        print("You are Lose")
    elif(computer== 0 and you ==-1):
        print("You are win")
    else:
        print("Something want wrong")    
    
    