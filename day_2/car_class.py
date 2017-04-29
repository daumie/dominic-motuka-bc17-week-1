"""SuperClass Car"""

class Car(object):
    """Contains boilerplate car information"""
    name = "General"
    model = "GM"
    num_of_doors = 4
    speed = 0

    def __init__(self, name="General", model="GM", car_type='car', num_of_wheels=4, num_of_doors=4):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_wheels = num_of_wheels
        self.num_of_doors = num_of_doors

        if self.car_type == "trailer":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

    def is_saloon(self):
        """Checks for saloon car"""
        if self.car_type != "trailer":
            return True
        else:
            return False

    def drive(self, gear):
        """Defines car speed when driving"""
        if self.car_type != "trailer":
            self.speed = int(gear * 1000 / 3)
            return self
        else:
            self.speed = gear * 11
            return self
            