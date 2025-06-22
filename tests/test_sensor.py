import unittest
import sys
import os

sys.path.append(os.getcwd())

from src.sensor import Sensor, ExitSensor, EntrySensor
from src.car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = EntrySensor(id=123, car_park=CarPark("123 Example Street", 100))

    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 123)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertEqual(self.entry_sensor.is_active, False)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.entry_sensor.car_park.plates), 1)


class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.exit_sensor = ExitSensor(id=234, car_park=CarPark("123 Example Street", 100))

    def test_exit_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 234)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)
        self.assertEqual(self.exit_sensor.is_active, False)

    def test_detect_vehicle(self):
        self.exit_sensor.car_park.plates = ["TEST-001", "TEST-002", "TEST-003"]
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.exit_sensor.car_park.plates), 2)


if __name__ == "__main__":
    unittest.main()