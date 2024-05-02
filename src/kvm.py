#!/bin/python3
import RPi.GPIO as GPIO
import time

#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


G_PIN = 17
#Initialize your pin
GPIO.setup(G_PIN,GPIO.OUT)

#Turn on the LED
print("LED on")
GPIO.output(G_PIN,1)

#Wait 3s
time.sleep(3)

#Turn off the LED
print("LED off")
GPIO.output(G_PIN,0)
