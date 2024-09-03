class Car:
    def __init__(self, license, max_speed) :
        self._current_speed = 0
        self._travelled_distance = 0
        self._license = license
        self._max_speed = max_speed

User_RegistrationNumber = input("Enter the license plate: ")
User_MaximumSpeed = input("Enter the car's maximum speed: ")
car = Car(User_RegistrationNumber, User_MaximumSpeed)

print(f"The car's current speed is: {car._current_speed}")
print(f"The car has travelled: {car._travelled_distance}")
print(f"The car license plate is: {car._license}")
print(f"The car's maximum speed is: {car._max_speed}")
