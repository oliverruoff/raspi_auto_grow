#!/usr/bin/env python3

import RPi.GPIO as gp

# Pins used for water pump and humidty sensor
PUMP_PIN = 18
HUMID_SENS_PIN = 21
HUMID_SENS_RELAY_PIN = 26

# Setting up the pins
gp.setmode(gp.BCM)
gp.setup(PUMP_PIN, gp.OUT)
gp.setup(HUMID_SENS_PIN, gp.IN)
gp.setup(HUMID_SENS_RELAY_PIN, gp.OUT)
# cleaning up the pins
gp.cleanup()
