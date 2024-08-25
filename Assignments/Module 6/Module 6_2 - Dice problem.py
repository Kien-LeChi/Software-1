print("The program will ask you for the number of sides of a dice"
      ", and will roll that dice until it gets the maximum value.")

import random

DiceSize = int(input("Enter the number of sides you want on your dice: "))
while 1 :
    num = random.randint(1, DiceSize)
    print(num)
    if num == DiceSize : exit()