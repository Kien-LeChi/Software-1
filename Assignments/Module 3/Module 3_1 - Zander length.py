zanLen = float(input("Enter zander length (in centimeters): "))
if zanLen < 42 :
    print(f"Please release the fish back into the lake as it is {42 - zanLen:<.5f}cm below the size limit")
else : print("Hooray! You caught a fish.")