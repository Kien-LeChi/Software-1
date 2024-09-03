import random

UserInput = int(input())
CustomList = [0]*110
for i in range(UserInput) :
    Spot = random.randint(1,100)
    CustomList[Spot] += 1

for i in range(1, 101):
    print(f"{CustomList[i] / UserInput : .2%}")
