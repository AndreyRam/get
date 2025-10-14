import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
bits = [22,27,17,26,25,21,20,16]
bits.reverse()

for i in range(len(bits)):
    GPIO.setup(bits[i], GPIO.OUT)

voltage = 3.3

def voltage_to_number(voltage):
    if(0<=voltage<=3.136):
        return (voltage/3.136 * 255)
    else:
        print("Выходит за пределы")
        return 0
    
def bin_arr(number):
    arr = [0]*8
    s = bin(int(number))[2:].zfill(8)
    for i in range(8):
        arr[i] = int(s[i])
    return arr

try:
    while True:
        try:
            voltage = float(input())
            num = voltage_to_number(voltage)
            bin_array = bin_arr(num)
            for i in range(8):
                GPIO.output(bits[i],bin_array[i])
        except ValueError:
            print("неверно")
finally:
    GPIO.output(bits,0)
    GPIO.cleanup()
