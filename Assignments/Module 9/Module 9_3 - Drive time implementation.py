class Car:

    # Task 1
    def __init__(self, license, max_speed):
        self._current_speed = 0
        self._travelled_distance = 0
        self._license = license
        self._max_speed = max_speed
        print(f"Your new car has a license plate of {license} and a maximum speed of {max_speed}.")
    # Task 1


    # Task 2
    def accelerate(self, _a_) : #_a_ == acceleration
        self._current_speed = max(0, self._current_speed + _a_)
        self._current_speed = min(self._current_speed, self._max_speed)
        if self._current_speed == 0:
            print("The vehicle has come to a full stop.")
        elif _a_ == 0 :
            print("The car's speed hasn't changed at all.")
        elif _a_ > 0:
            print(f"The car's speed have increased to {self._current_speed}.")
        else :
            print(f"The car's speed have decreased to {self._current_speed}.")


    def EmergencyBrake(self) :
        self.accelerate(-200)
    # Task 2


    # Task 3
    def drive(self, hours) :
        self._travelled_distance += hours * self._current_speed
        print(f"The car has travelled {self._travelled_distance}")
    # Task 3


carr = Car('ABC-123', 300)
carr._current_speed = 60
carr.drive(1.5)

