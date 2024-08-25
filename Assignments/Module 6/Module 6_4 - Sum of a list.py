print("This program will take an integer list as input,"
      " and will calculate its sum using a function.")
def SumList(UserList) :
    sum = 0
    for i in range(len(UserList)) :
        sum += int(UserList[i])
    return sum

InputList = []
while 1 :
    UserNumber = input("Enter your number (Or blank to stop) : ")
    try :
        num = int(UserNumber)
        InputList.append(num)
    except : break
print(SumList(InputList))