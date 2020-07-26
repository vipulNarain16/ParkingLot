import unittest
from basic_parkinglot import basic_parkinglot

class test_parkinglot(unittest.TestCase):
    def test_createparkinglot(self):
        parkingLot = basic_parkinglot()
        result = parkingLot.createparkinglot(10)
        self.assertEqual(10, result)


    def test_park_vechicle(self):
        parkingLot = basic_parkinglot()
        result = parkingLot.createparkinglot(2)
        result = parkingLot.park_vechicle("KA-01-SA-0000", "White")
        result = parkingLot.park_vechicle("UP-21-QQ-1111", "Blue")
        self.assertNotEqual(-1, result)

    def test_print_details(self):
        parkingLot = basic_parkinglot()
        result = parkingLot.createparkinglot(2)
        result = parkingLot.park_vechicle("KA-01-SA-0000", "White")
        result = parkingLot.park_vechicle("UP-21-QQ-1111", "Blue")
        result = parkingLot.print_details()

    def test_remove(self):
        parkingLot = basic_parkinglot()
        result = parkingLot.createparkinglot(2)
        result = parkingLot.park_vechicle("KA-01-SA-0000", "White")
        result = parkingLot.park_vechicle("UP-21-QQ-1111", "Blue")
        result = parkingLot.remove(2)
        self.assertEqual(1, result)

    def test_get_details(self):
        parkingLot = basic_parkinglot()
        result = parkingLot.createparkinglot(2)
        result = parkingLot.park_vechicle("KA-01-SA-0000", "White")
        result = parkingLot.park_vechicle("UP-21-QQ-1111", "Blue")
        result = parkingLot.get_details("KA-01-SA-0000", "White")
        self.assertNotEqual(1, result)

if __name__ == 'main':
    unittest.main()

