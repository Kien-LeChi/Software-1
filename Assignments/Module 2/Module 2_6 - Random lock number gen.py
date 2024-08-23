import random as rand
print(f"Your 3-digit code is: {rand.randint(0,999):0=3}")
print("Your 4-digit code is: ", end = '')
for i in range(0, 4) :
    print(rand.randint(1, 6), end = '')