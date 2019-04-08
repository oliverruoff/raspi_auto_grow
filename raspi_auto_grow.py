import RPi.GPIO as gp
import time
from datetime import datetime

PUMP_PIN = 20
HUMID_SENS_PIN = 21

gp.setmode(gp.BCM)

gp.setup(PUMP_PIN, gp.OUT)
gp.setup(HUMID_SENS_PIN, gp.IN)


def soil_is_try():
    return gp.input(HUMID_SENS_PIN)


def run_pump():
    gp.output(PUMP_PIN, gp.HIGH)
    time.sleep(5)
    gp.output(PUMP_PIN, gp.LOW)


if __name__ == '__main__':
    while(True):
        if soil_is_try():
            print(datetime.now(), 'Soil seems to be try, watering the plant now.')
            run_pump()
        else:
            print(datetime.now(), 'Soil seems to be humid, won\'t water the plant.')
        time.sleep(20)
