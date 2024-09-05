print("This program will check whether your input number is prime.")

num = int(input("Enter a number: "))

i = 2
checker = False
if num == 1 : print("Your number is not a prime.")
elif num == 2 : print("Your number is prime.")
else :
    while(i * i <= num) : #i <= sqrt(num) --> O(sqrt(n))
        if num % i == 0 :
            print("Your number is not a prime.")
            checker = True
            break
        else : i += 1
    if checker == 0 : print("Your number is prime.")