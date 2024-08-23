inch = float(input("Enter your inch value: "))
while inch > 0 :
    print(f"Your converted value is {inch * 2.54 : <.5f}cm.")
    inch = float(input("Enter your inch value: "))
print("Program ends.")