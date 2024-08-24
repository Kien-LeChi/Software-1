print("This program describe your cabin class.")
cabClass = str(input("Please enter your cabin class (LUX / A / B / C): "))
if cabClass == 'LUX' :
    print("LUX: upper-deck cabin with a balcony.")
elif cabClass == 'A' :
    print("A: above the car deck, equipped with a window.")
elif cabClass == 'B' :
    print("B: windowless cabin above the car deck.")
elif cabClass == 'C' :
    print("C: windowless cabin below the car deck.")
else : print("Invalid cabin class.")