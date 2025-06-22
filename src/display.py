class Display:
    def __init__(
        self,
        id,
        message = "" ,
        is_on = False,
        car_park = None
    ):
        self.id = id
        self.message = message or {"message": message}
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f'Display \
            {self.id}: \
            {self.message}'
    
    def update(self, data):
        """
        Outputs message data to displays.
        """
        if type(self.message) == str:
            self.message = data
        else: self.message.update(data)
        for key, value in data.items():
            print(f"{key}: {value}")
