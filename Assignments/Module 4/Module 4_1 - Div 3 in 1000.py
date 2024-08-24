import time
print("I will start printing every multiplier of 3 less than 1000 in", end = ' ')

cnt = 3
while cnt > 0 :
    print(cnt, end = ' ')
    cnt -= 1
    time.sleep(1)
print()

num = 3
while num <= 1000 :
    print(num)
    num += 3