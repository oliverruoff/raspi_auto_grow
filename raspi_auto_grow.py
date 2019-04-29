#!/usr/bin/env python3

'''
Script to run a humidity sensor and a 5 volts water pump

Note:
Have to set pin to "IN", since taking away 3,3V (from raspi),
it isn't enough to turn off the relays with setting pin to LOW
'''

import RPi.GPIO as gp
import time
from datetime import datetime
from notify_run import Notify

# Pins used for water pump and humidity sensor
PUMP_PIN = 18
HUMID_SENS_PIN = 21
HUMID_SENS_RELAY_PIN = 26

# Check interval time
CHECK_INTERVAL_IN_SECONDS = 20
# How long the water pump will pump in one run
PUMP_TIME = 5

# Variable to monitor sensor dying
watered_in_row = 0

# For Android notifications
notify = Notify()

# Setting up the pins
gp.setmode(gp.BCM)
gp.setup(HUMID_SENS_PIN, gp.IN)
gp.setup(HUMID_SENS_RELAY_PIN, gp.IN)


def soil_is_dry():
    '''Checks if the soil is dry or moist.

    Returns:
        boolean -- True if dry, else False
    '''
    # Activating humidity sensor relay
    gp.setup(HUMID_SENS_RELAY_PIN, gp.OUT)
    gp.output(HUMID_SENS_RELAY_PIN, gp.HIGH)
    time.sleep(0.5)
    # Reading sensor pin
    humid = gp.input(HUMID_SENS_PIN)
    # Deactivating humidity sensor relay to take away voltage
    # from sensor
    gp.setup(HUMID_SENS_RELAY_PIN, gp.IN)
    return humid


def run_pump():
    '''Activating the water pump for `PUMP_TIME` seconds.
    '''
    # Activating pump (HIGH / LOW is not enough for 5v relays)
    gp.setup(PUMP_PIN, gp.OUT)
    gp.output(PUMP_PIN, gp.HIGH)
    # Waiting for water to flow
    time.sleep(PUMP_TIME)
    # Deactivating pump
    gp.setup(PUMP_PIN, gp.IN)


if __name__ == '__main__':
    while(True):
        if soil_is_dry():
            watered_in_row += 1
            if watered_in_row < 5:
                print(datetime.now(),
                      'Soil seems to be dry, watering the plant now.')
                notify.send(str(datetime.now().strftime(
                    "%H:%M")) + ' > Watering :)')
            else:
                print(datetime.now(),
                      'Soil seems to be dry, watering the plant now.')
                print('[WARNING] Watered', watered_in_row,
                      'in a row, humidity sensor might be defect!')
                notify.send(str(datetime.now().strftime(
                    "%H:%M")) + ' > Watering :) [SENSOR WARNING] <' +
                    str(watered_in_row) + '>')
            run_pump()
        else:
            watered_in_row = 0
            print(datetime.now(),
                  'Soil seems to be humid, won\'t water the plant.')
        time.sleep(CHECK_INTERVAL_IN_SECONDS)
