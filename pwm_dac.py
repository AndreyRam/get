import RPi.GPIO as GPIO
import time


class pwm_:
    def __init__(self):
        self.highest_lvl = 3.275
        self.bit = 12
        self.duty = 0.0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bit, GPIO.OUT)

        self.pwm = GPIO.PWM(12, 1000)
        self.pwm.start(self.duty)

    def set_voltage(self,volt):

        self.pwm.ChangeDutyCycle(volt/self.highest_lvl*100)
        #print(volt/self.highest_lvl)
    
    def deinit(self):
        GPIO.output(self.bit,0)
        GPIO.cleanup()

my_plate = pwm_()


if __name__ == "__main__":
    try:
        while True:
            try:
                
                n = float(input("input digit:"))
                my_plate.set_voltage(float(n  + (n-2)*0.2))
            except ValueError:
                print("ошибка")
    finally:
        my_plate.deinit()
