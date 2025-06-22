from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(
        self,
        id,
        is_active = False,
        car_park = None
    ):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f'Sensor ID: \
            {self.id}: Sensor Status: \
            {self.is_active}'
    
    @abstractmethod
    def update_car_park(self, plate):
        """
        Updates CarPark plates list by appending or removing number plate id.
        """
        pass
    
    def _scan_plate(self):
        """
        Simulates a number plate scanner to return a random plate id.
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """
        When vehicle is detected by a sensor the number plate is scanned and
        the CarPark is updated with the plate information.
        """
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def _scan_plate(self):
        """
        Simulates a plate scanner by returning a plate id that has been
        previously scanned into the carpark.
        """
        return random.choice(self.car_park.plates)
    
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
