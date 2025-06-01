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

