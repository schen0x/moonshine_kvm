#!/bin/python3
import RPi.GPIO as GPIO
import time
import sys

G_PIN = 27;

def init():
    #GPIO Basic initialization
    GPIO.setmode(GPIO.BCM);
    GPIO.setwarnings(False);
    #Initialize your pin
    GPIO.setup(G_PIN,GPIO.OUT);
    return;


def GPIO_PRESS(time_in_seconds):
    """
    Press the button for <time_in_seconds> on demand.
    Exit gracefully (must release when interrupted)
    """
    try:
        #Turn on the LED
        GPIO.output(G_PIN,1);
        print("pressed");
        #Wait <time_in_seconds> seconds
        time.sleep(time_in_seconds);
    finally:
        #Turn off the LED
        GPIO.output(G_PIN,0);
        print("released");
        return;


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["on", "off"]:
        print("Usage: ./<thisScript> <on | off>");
        exit(1);

    init();
    if sys.argv[1] == "on":
        print("power on")
        GPIO_PRESS(2);
    elif sys.argv[1] == "off":
        print("power off")
        GPIO_PRESS(6);
