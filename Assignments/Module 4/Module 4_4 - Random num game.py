import random as rand
num = rand.randint(1, 10)
userInput = 0
while True :
    userInput = int(input("Guess the number between 1 and 10: "))
    if(userInput < num) : print("Too low")
    elif(userInput > num) : print("Too high")
    else :
        print("Correct")
        break
