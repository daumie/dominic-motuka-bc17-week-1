"""Contains tests for the car class OOP"""
import unittest
from day_2.car_class import Car

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        """Test for proper inheritance"""
        honda = Car('Honda')
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        """Tests for car type inheritance"""
        honda = Car('Honda')
        self.assertTrue(isinstance(honda, Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        """Test default car name attribute"""
        car_name = Car()
        self.assertEqual('General', car_name.name,
                         msg='The car should be called `General`,'+
                         ' if no name was passed as an argument')

    def test_default_car_model(self):
        """Tests for default car model"""
        car_model = Car()
        self.assertEqual('GM', car_model.model, msg="The car's model should be called `GM`"+
                         " if no model was passed as an argument")

    def test_car_properties(self):
        """Tests car properties"""
        toyota = Car('Toyota', 'Corolla')
        self.assertListEqual(['Toyota', 'Corolla'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        """Tests for number of car doors default is 4"""
        opel = Car('Opel', 'Omega 3')
        porshe = Car('Porshe', '911 Turbo')
        self.assertListEqual([opel.num_of_doors,
                              porshe.num_of_doors,
                              Car('Koenigsegg', 'Agera R').num_of_doors], [4, 2, 2],
                             msg='The car shoud have four (4) doors'+
                             ' except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        """Tests the number of wheels a car has , default is 4"""
        man = Car('MAN', 'Truck', 'trailer')
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                         msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        """Tests fro the car type"""
        koenigsegg = Car('Koenigsegg', 'Agera R')
        self.assertTrue(koenigsegg.is_saloon(),
                        msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        """Tests for the car speed for moving car"""
        man = Car('MAN', 'Truck', 'trailer')
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 77],
                             msg='The Trailer should have speed 0 km/h'+
                             ' until you put `the pedal to the metal`')

    def test_car_speed2(self):
        """Tests car speed for stationery car"""
        man = Car('Mercedes', 'SLR500')
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed], [0, 1000],
                             msg='The Mercedes should have speed 0 km/h until '+
                             'you put `the pedal to the metal`')

    def test_drive_car(self):
        """Tests for inheritance of a moving car"""
        man = Car('MAN', 'Truck', 'trailer')
        moving_man = man.drive(7)
        moving_man_instance = isinstance(moving_man, Car)
        moving_man_type = isinstance(moving_man, Car)
        self.assertListEqual([True, True, man.speed],
                             [moving_man_instance, moving_man_type, moving_man.speed],
                             msg='The car drive function should return'+
                             ' the instance of the Car class')

if __name__ == '__main__':
    unittest.main()
    