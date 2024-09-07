class Car:

    def __init__(self,  license, max_speed):
        self.current_speed = 0
        self.travelled_distance = 0
        self.license = license
        self.max_speed = max_speed


    def accelerate(self, _a_) : #_a_ == acceleration
        self.current_speed = max(0, self.current_speed + _a_)
        self.current_speed = min(self.current_speed, self.max_speed)


    def emergency_brake(self) :
        self.accelerate(-200)


    def drive(self, hours) :
        self.travelled_distance += hours * self.current_speed


    def output_properties(self):
        print(f"License plate: {self.license}")
        print(f"Max speed: {self.max_speed}km/h")
        print(f"Current speed: {self.current_speed}km/h")
        print(f"Travelled distance: {self.travelled_distance}km\n")

class ElectricCar(Car) :

    def __init__(self, license, max_speed, battery_capacity) :
        Car.__init__(self, license, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car) :

    def __init__(self, license, max_speed, tank_volumn) :
        Car.__init__(self, license, max_speed)
        self.tank_volumn = tank_volumn

Car1 = ElectricCar("ABC-15", 180, 52.5)
Car2 = GasolineCar("ACD-123", 165, 32.3)


import random as rand
Car1.current_speed = rand.randint(100, 200)
Car2.current_speed = rand.randint(100, 200)

Car1.drive(3)
Car2.drive(3)

Car1.output_properties()
Car2.output_properties()