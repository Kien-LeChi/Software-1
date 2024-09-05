class Car:

    def __init__(self,  license_, max_speed):
        self.current_speed = 0
        self.travelled_distance = 0
        self.license = license_
        self.max_speed = max_speed


    def accelerate(self, _a_) : #_a_ == acceleration
        self.current_speed = max(0, self.current_speed + _a_)
        self.current_speed = min(self.current_speed, self.max_speed)


    def emergency_brake(self) :
        self.accelerate(-200)


    def drive(self, hours) :
        self.travelled_distance += hours * self.current_speed


    def output_properties(self):
        print(self.current_speed, end = " ")
        print(self.travelled_distance, end = ' ')
        print(self.license, end = ' ')
        print(self.max_speed, end = '\n')


import random

cars = [Car(0, 0)] * 10
for i in range(10) :
    individualMaxSpeed = random.randint(100, 200)
    cars[i] = Car(f"ABC-{i + 1}", individualMaxSpeed)

NoCarsWon = True
while True:
    for i in range(10) :
        if cars[i].travelled_distance >= 10000 :
            NoCarsWon = False
    if NoCarsWon == 0 : break
    for i in range(10) :
        cars[i].accelerate(random.randint(-10, 15))
        cars[i].drive(1)


print(f"{'No.' :^5}| Registration Number | Current speed | Travelled distance | Max Speed |")
for i in range(10) :
    print(f"{i + 1 : ^5}| "
          f"{cars[i].license:^20}|"
          f"{cars[i].current_speed :^15}|"
          f"{cars[i].travelled_distance:^20}|"
          f"{cars[i].max_speed :^11}|")