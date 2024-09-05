#Muc tieu : chia het cho 3 trong 1 - 1000
#3 6 9 12 ... 999

a = 3
while True :
    print(a)
    a = a + 3
    if a >= 1000 : break

a = 3
while a < 1000 :
    if a % 3 == 0 : print(a)
    a = a + 1
    # if a >= 1000: break
# a range (for) 1 --> 1000
# a % 3 == 0 --> print(a)
