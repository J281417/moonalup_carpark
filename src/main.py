from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

import sys
import os

sys.path.append(os.getcwd())

def main():
    car_park = CarPark(location="moondalup",
                       capacity=100,
                       log_file="moondalup.txt",
                       config_file="moondalup_config.json"
                       )
    car_park.write_config()

    moondalup_car_park = CarPark.from_config(config_file="moondalup_config.json")

    entry_sensor = EntrySensor(id=1,
                               is_active=True,
                               car_park=moondalup_car_park)

    exit_sensor = ExitSensor(id=2,
                             is_active=True,
                             car_park=moondalup_car_park)

    display = Display(id=1,
                      is_on=True,
                      car_park=moondalup_car_park,
                      message="Welcome to Moondalup")

    moondalup_car_park.register(entry_sensor)
    moondalup_car_park.register(exit_sensor)
    moondalup_car_park.register(display)

    for _ in range(10):
        entry_sensor.detect_vehicle()

    for _ in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
