class Sensor:
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

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...
    