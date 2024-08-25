def  OddNumbersRemove(InputList) :
    OutputList = []
    for i in range(len(InputList)) :
        if InputList[i] % 2 == 0 : OutputList.append(InputList[i])
    return OutputList

TestList = []

#Creating a list
ListLength = int(input("Enter your list length: "))
print("Now please enter in your number list: ", end = '')
for i in range(ListLength) :
    TestList.append(int(input()))

print(OddNumbersRemove(TestList))
