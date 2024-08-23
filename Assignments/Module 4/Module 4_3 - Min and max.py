import math

mini = float('inf')
maxi = float('-inf')

while True :
    val = input("Enter a number (or an empty string to stop program): ")
    try:
        mini = min(mini, float(val))
        maxi = max(maxi, float(val))
    except: break
if mini == float('inf') or maxi == float('-inf') : print("No number was entered.")
else : print(f"The smallest number is: {mini} and the largest number is: {maxi}")


