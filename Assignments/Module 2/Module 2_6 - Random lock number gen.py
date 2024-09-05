import random as rand
print("This program generates 2 random lock numbers")

#3 digit code
print(f"Your 3-digit code is: {rand.randint(0,999):0>3}")
#End 3 digit code

print("awduh", end = '')
print('auahwiud')

#4 digit code
print("Your 4-digit code is: ", end = '')
for i in range(0, 4) :
    print(rand.randint(1, 6), end = '')
#End 4 digit code