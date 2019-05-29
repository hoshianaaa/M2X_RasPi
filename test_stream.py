#!/usr/bin/env python

import os 
import time
from m2x.client import M2XClient

client = M2XClient(key=os.environ['API_KEY'])
device = client.device(os.environ['DEVICE_ID'])
stream = device.stream(os.environ['stream_name'])
stream_2 = device.stream(os.environ['stream_name_2'])

import sys
sys.path.append('/home/pi/Downloads/DHT11_Python')
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        stream.add_value(result.temperature)
        stream_2.add_value(result.humidity)
        time.sleep(10)

    time.sleep(1)
