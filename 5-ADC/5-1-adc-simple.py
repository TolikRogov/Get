import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    for val in range(256):
        GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
        val_in_comp = GPIO.input(comp)
        time.sleep(0.01)
        if val_in_comp:
            return val
    return 0

try:
    while True:
        value = adc()
        volt = value * 3.3 / 256.0
        print("{:.2f)V".format(volt))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
