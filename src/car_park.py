from display import Display
from sensor import Sensor

class CarPark:
    def __init__(
        self,
        location,
        capacity,
        plates=None,
        sensors=None,
        displays=None
    ):
        self.location = location
        self.sensors = sensors or []
        self.capacity = capacity
        self.plates = plates
        self.displays = displays

    def __str__(self):
        return f'Car park at  \
            {self.location} with \
            {self.capacity} bays'

    def register(
            self,
            component = Sensor | Display
    ):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.sensors.append(component)

    def add_car(
            self,
            plate
    ):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(
            self,
            plate
    ):
        self.plates.pop(plate)
        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update(
                {
                    "Available_bays": self.available_bays,
                    "Temperature": 25
                }
                )

    @property
    def available_bays(self):
        return 0 if self.capacity - len(self.plates) < 0 else self.capacity - len(self.plates)
