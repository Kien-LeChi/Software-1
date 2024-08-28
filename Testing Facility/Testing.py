import random
a = [0]*15
#The array have 12 slots, initially being all 0's
num = input("Enter a number: ")
num = int(num)
for i in range(int(num)) :
    x = random.randint(1, 6) + random.randint(1, 6)
    a[x] += 1
    #When the sum is x, the array at position 'x' is increased by 1
    #So basically it counts how many times the sum 'x' presents in all
    #rolls
for i in range(2, 13) :
    print(f"There are total {a[i] / num:.2%} rolls summed to {i}")