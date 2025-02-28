import RPi.GPIO as GPIO

pin = 21
led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(pin, 1000)
pwm.start(0)

try:
	while True:
		number = int(input("Enter your duty cycle: "))
		pwm.ChangeDutyCycle(number)
		print(3.3 * number / 100)

finally:
	pwm.stop()
	GPIO.output(pin, 0)
	GPIO.cleanup()
