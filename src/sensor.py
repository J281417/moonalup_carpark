from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(
        self,
        id,
        is_active = "",
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
        pass
    
    def _scan_plate(self):
        return random.choice(self.car_park.plates)
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
