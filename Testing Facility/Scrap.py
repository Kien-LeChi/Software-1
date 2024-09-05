#Kiem tra n co phai so nguyen to hay kh
#n la so nguyen to <=> n chia het cho 1 va chinh no.
# <=> n ko chia het cho 2 -> n - 1

n = int(input())
if n == 1 : print('n ko la so nguyen to')
elif n == 2 : print('n la so nguyen to')
else :
    for i in range(2, n) :
        if(n % i == 0) :
            break
    if i == n - 1 : print("n la so nguyen to")
    else : print("n ko la so nguyen to")
O(n)