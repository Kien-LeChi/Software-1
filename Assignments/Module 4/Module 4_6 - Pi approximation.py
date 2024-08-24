import random as rand

insideCircle = 0
TotalPointsGen = int(input("Enter the number of points to generate for pi approximation: "))
for i in range(0, TotalPointsGen) :
    x = rand.random()
    y = rand.random()
    if x*x + y*y < 1 : insideCircle += 1
print(f"Your pi approximation is: {4 * insideCircle / TotalPointsGen: <.10f}")