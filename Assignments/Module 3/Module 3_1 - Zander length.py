print("This program tells you whether your zander fulfill the size limit or not")
zanderLength = float(input("Enter zander length (in centimeters): "))
if zanderLength < 42 :
    print(f"Please release the fish back into the lake as it is "
          f"{42 - zanderLength:<.2f}cm below the size limit")
else : print("Hooray! You caught a fish.")