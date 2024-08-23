numList = []
while True :
    num = input('Enter a number (Or "stop" to stop the program): ')
    try:
        numList.append(float(num))
    except :
        if num == 'stop' : break
        else : print('Invalid input')

numList.sort(reverse = True)
if len(numList) < 5 :
    print("There is less than 5 numbers in the list.")
for i in range(5) :
    print(numList[i], end = ' ')