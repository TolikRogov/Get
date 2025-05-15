import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
	return [int(bit) for bit in bin (value)[2:].zfill(8)]

number = 0
flag = 0
try:
	per = float(input("Enter your period of signal: "))

	while True:
		GPIO.output(dac, decimal2binary(number))

		if flag == 1:
			number -= 1
		else:
			number += 1

		if number == 255:
			flag = 1
		if number == 0:
			flag = 0

		time.sleep(per / 512)

finally:
	GPIO.output(dac, 0)
	GPIO.cleanup()
