print("This program will print out 5 greatest number"
      "from the set of inputted numbers in descending order.")

numList = []
while True :
    num = input('Enter a number (Or an empty string to stop the program): ')
    try:
        numList.append(float(num))
    except :
        if num == '' : break
        else : print('Invalid input')

numList.sort(reverse = True)
if len(numList) < 5 :
    print("There is less than 5 numbers in the list.")
    exit()
print("The five greatest numbers in descending order are: ", end = '')
for i in range(5) :
    print(numList[i], end = ' ')