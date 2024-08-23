num = int(input("Enter a number: "))
i = 2
checker = False
if num <= 2 :
    print("Your number is prime.")
    exit()
else :
    while(i * i <= num) :
        if num % i == 0 :
            print("Your number is not a prime.")
            checker = True
            break
        else :
            i += 1
if checker == 0 : print("Your number is prime.")