import RPi.GPIO as GPIO

def bin_arr(number):
    arr = [0]*8
    s = bin(int(number))[2:].zfill(8)
    for i in range(8):
        arr[i] = int(s[i])
    return arr

class R2R_DAC:
    def __init__(self):
        self.works = [22,27,17,26,25,21,20,16]
        self.works.reverse()
        self.bits = [0]*8

        self.highest_lvl = 3.136

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.works, GPIO.OUT)

    def set_number(self, number):
        if(0 <= number <= 255 ):
            bin_array = bin_arr(number)
            
            for i in range(8):
                self.bits[i] = int(bin_array[i])
            for i in range(8):
                #print(bits[i])
                GPIO.output(self.works[i],self.bits[i])
        else:
            print("неверное число")

    def set_voltage(self, v):
        num = int(v / self.highest_lvl * 255)
        self.set_number(num)

    def deinit(self):
        #print(bits)
        GPIO.output(self.works,0)
        GPIO.cleanup()



if __name__ == "__main__":
    try:
        my_plate = R2R_DAC()
        while True:
            try:
                s = input()
                n = float(input())
                if(s == 'v'):
                    my_plate.set_voltage(float(n))
                else:
                    my_plate.set_number(float(n))
            except ValueError:
                print("неверно")
    finally:
        my_plate.deinit()
