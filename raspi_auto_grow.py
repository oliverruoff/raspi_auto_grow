import RPi.GPIO as gp
import time
from datetime import datetime
from notify_run import Notify

# Pins used for water pump and humidty sensor
PUMP_PIN = 20
HUMID_SENS_PIN = 21

# Check interval time
CHECK_INTERVAL_IN_SECONDS = 20
# How long the water pump will pump in one run
PUMP_TIME = 5

# For Android notifications
notify = Notify()

# Setting up the pins
gp.setmode(gp.BCM)
gp.setup(PUMP_PIN, gp.OUT)
gp.setup(HUMID_SENS_PIN, gp.IN)


def soil_is_dry():
    '''Checks if the soil is dry or moist.

    Returns:
        boolean -- True if dry, else False
    '''

    return gp.input(HUMID_SENS_PIN)


def run_pump():
    '''Activating the water pump for `PUMP_TIME` seconds.
    '''

    gp.output(PUMP_PIN, gp.HIGH)
    time.sleep(PUMP_TIME)
    gp.output(PUMP_PIN, gp.LOW)


if __name__ == '__main__':
    while(True):
        if soil_is_dry():
            print(datetime.now(),
                  'Soil seems to be dry, watering the plant now.')
            notfiy.send(str(datetime.now()) + ' > Watering the plant :)')
            run_pump()
        else:
            print(datetime.now(),
                  'Soil seems to be humid, won\'t water the plant.')
        time.sleep(CHECK_INTERVAL_IN_SECONDS)
