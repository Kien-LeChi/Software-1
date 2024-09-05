class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor


    def floor_up(self):
        self.current_floor = min(self.top_floor, self.current_floor + 1)
        print(f"The elevator is on {self.current_floor}")


    def floor_down(self):
        self.current_floor = max(self.bottom_floor, self.current_floor - 1)
        print(f"The elevator is on {self.current_floor}")


    def go_to_floor(self, floor):
        check = True
        if floor < self.bottom_floor or floor > self.top_floor :
            print("The floor is out of range. Please try again.")
            check = False
        while self.current_floor < floor and check :
            self.floor_up()

        while self.current_floor > floor and check :
            self.floor_down()

