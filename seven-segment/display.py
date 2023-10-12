# seven-segment module support functions
# Author: Eddy Ferre - ferree@seattleu.edu

import RPi.GPIO as GPIO
from time import sleep
from .constants import *


# noinspection PyUnusedLocal
def init_display(channels_set):
    GPIO.setwarnings(False)
    # Setup and Initialize the GPIO pins
    GPIO.setmode(GPIO.BCM)
    for pin in OUT_PINS:
        GPIO.setup(pin, GPIO.OUT)
    for pin in IN_PINS:
        GPIO.setup(pin, GPIO.IN)
    channels_set = True
    clear_displays()


def activate_displays(digits, decimal_point=None, set_colon=False, set_thousand=False):
    if decimal_point is None:
        decimal_point = [False] * 4
    for d in range(4):
        # Set the display pins
        GPIO.output(DISP_OUT_L[d - 1], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d - 2], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d - 3], GPIO.HIGH)
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


def clock_displays(digits):

    for d in range(4):
        # Set the display pins
        GPIO.output(DISP_OUT_L[d - 1], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d - 2], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d - 3], GPIO.HIGH)
        GPIO.output(DISP_OUT_L[d], GPIO.LOW)

        # Set the 7-segment
        for seg_index in range(7):
            GPIO.output(SEGMENT_OUT_H[seg_index], SEGS_FOR_CHAR[digits[d]][seg_index])

        sleep(0.005)


def clear_displays():
    for pin in ACTIVE_HIGH_PINS:
        GPIO.output(pin, GPIO.LOW)
    for pin in ACTIVE_LOW_PINS:
        GPIO.output(pin, GPIO.HIGH)


def set_colon(state):
    GPIO.output(COLON_OUT_H, state)


def set_led(state):
    GPIO.output(LED_OUT_H, state)


def get_button_pressed():
    return GPIO.input(BUTTON_IN) == GPIO.LOW


def cleanup(channels_set):
    if channels_set:
        GPIO.cleanup()
