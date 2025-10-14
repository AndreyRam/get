import smbus
import RPi.GPIO as GPIO
import time
import numpy
import math

def get_sin_wave_amplitude(freq, time):
    sinus = math.sin(2 * 3.1415926535 * freq * time) 
    return (sinus + 1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)
