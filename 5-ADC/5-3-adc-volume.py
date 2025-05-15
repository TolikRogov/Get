import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9][::-1]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def adc():
	val = 128
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 128

	val = 64
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 64

	val = 32
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 32

	val = 16
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 16

	val = 8
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 8

	val = 4
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 4

	val = 2
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 2

	val = 1
	GPIO.output(dac, [int(bit) for bit in bin (val)[2:].zfill(8)])
	time.sleep(0.01)
	if GPIO.input(comp):
		val -= 1

	return val


try:
    while True:
        value = adc()
        volt = value * 3.3 / 256.0
        print("{:.2f)V".format(volt))
        array = [0] * 8
        for i in range(int(value / 256 * 10) - 1):
            array[i] = 1
        GPIO.output(leds, array)


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
