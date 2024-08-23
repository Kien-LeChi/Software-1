import random as rand

TotalDice = int(input("Enter how many dices you want to roll: "))
dice = 0
SumOfDice = 0;

for i in range(TotalDice) :
    dice = rand.randint(1, 6)
    SumOfDice += dice

print("The sum of all dice results is {sum}".format(sum=SumOfDice))