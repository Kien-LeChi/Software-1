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
class Race :


    def __init__(self, name, kilometers, list_of_cars):
        self._hour_passed = 0
        self._name = name
        self._distance = kilometers
        self._list_of_cars = list_of_cars
        self._total_cars = len(list_of_cars)

    def hour_passes(self):
        for i in range(self._total_cars):
            self._list_of_cars[i].accelerate(random.randint(-10, 15))
            self._list_of_cars[i].drive(1)

        self._hour_passed += 1


    def print_status(self):
        print(f"Hour {self._hour_passed}")
        print(f"{'No.' :^5}| Registration Number | Current speed | Travelled distance | Max Speed | ")
        for i in range(self._total_cars):
            print(f"{i + 1 : ^5}| "
                  f"{self._list_of_cars[i].license:^20}|"
                  f"{self._list_of_cars[i].current_speed :^15}|"
                  f"{self._list_of_cars[i].travelled_distance:^20}|"
                  f"{self._list_of_cars[i].max_speed :^11}|")

    def race_finished(self):
        for i in range(self._total_cars) :
            if self._list_of_cars[i].travelled_distance >= self._distance :
                return True

        return False

cars = [Car(0, 0)] * 10
for i in range(10) :
    individualMaxSpeed = random.randint(100, 200)
    cars[i] = Car(f"ABC-{i + 1}", individualMaxSpeed)

Main_Race = Race("Grand Demolition Derby", 8000, cars)

while Main_Race.race_finished() == 0 :
    Main_Race.hour_passes()

    if(Main_Race._hour_passed % 10 == 0) :
        Main_Race.print_status()
        print()

print("The race has ended.")
Main_Race.print_status()