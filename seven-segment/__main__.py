#!/usr/bin/python

# seven-segment module Main function
# Author: Eddy Ferre - ferree@seattleu.edu

import RPi.GPIO as GPIO
from traceback import print_exc
from sys import stdout
from re import match, compile
from time import sleep

from .constants import *


def activate_displays (digits, decimal_point=[False]*4, set_colon=False, set_thousand=False):
    for d in range(4):
        # Set the display pins
        GPIO.output(DISP_OUT_L[d-1], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d-2], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d-3], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d], GPIO.LOW)

        # Set the colon and thousand
        GPIO.output(COLON_OUT_H, d == 1 and set_colon)
        GPIO.output(THOUSAND_OUT_H, d == 2 and set_thousand)

        # Set decimal point
        GPIO.output(DP_OUT_H, decimal_point[d])
        
        # Set the 7-segment
        for seg_index in range(7):
            GPIO.output(SEGMENT_OUT_H[seg_index], SEGS_FOR_CHAR[digits[d]][seg_index])

        sleep(0.005)


def main():
    channels_set = False
    try:

        # Setup and Initialize the GPIO pins
        GPIO.setmode(GPIO.BCM)
        for pin in OUT_PINS:
            GPIO.setup(pin, GPIO.OUT)
        channels_set = True
        for pin in ACTIVE_HIGH_PINS:
            GPIO.output(pin, GPIO.LOW)
        for pin in ACTIVE_LOW_PINS:
            GPIO.output(pin, GPIO.HIGH)

        # Let user enter 4 characters
        string = input("Enter what you want the clock display to print: ")

        # Parse Clock entry
        clock_pattern = compile(f"([12]?)(\d):([0-5])(\d)")
        m = clock_pattern.match(string)
        if m is None:
            pass
        elif m.group(1) == '2' and m.group(2) not in "0123":
            raise ValueError("Clock - Invalid entry")
        else:
            print("Valid clock entry")
            # Sets the Digits
            if m.group(1) == '':
                digits = " "
            else:
                digits = m.group(1)
            for i in range(2, 5):
                digits += m.group(i)
            while True:
                activate_displays(digits, set_colon=True)

        # Parse number
        try:
            value = float(string)
            print("Valid number")
            # TODO: write your code here!
            # Watch for negative values, floating points...
        except ValueError:
            pass
            
        digits = "-Err"
        while True:
            activate_displays(digits)

    except KeyboardInterrupt:
        print()
        print("Ctrl+C pressed, exiting")
    except ValueError as e:
        print(e)
    except Exception:
        print("-"*60)
        print_exc(file=stdout)
        print("-"*60)
    finally:
        if channels_set:
            GPIO.cleanup()


if __name__ == "__main__":
    main()
