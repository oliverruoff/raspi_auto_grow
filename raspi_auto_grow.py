import RPi.GPIO as gp
import time
from notify_run import Notify

# Pins used for water pump and humidty sensor
PUMP_PIN = 20
HUMID_SENS_PIN = 21

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

    gp.setup(PUMP_PIN, gp.OUT)
    gp.output(PUMP_PIN, gp.HIGH)
    time.sleep(PUMP_TIME)
    # Have to set pin to "IN", since taking away 3,3V (from raspi)
    # isn't enough to turn off the pump
    gp.setup(PUMP_PIN, gp.IN)
