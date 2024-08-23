import random
def DiceRoll() :
    return random.randint(1,6)

while(1) :
    num = DiceRoll()
    print(num)
    if(num == 6) : break