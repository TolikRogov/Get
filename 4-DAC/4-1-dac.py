import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
	return [int(bit) for bit in bin (value)[2:].zfill(8)]

try:
	while True:
		number = input("Enter a number in range [0, 255]: ")
		try:
			number = int(number)
			if 0 <= number <= 255:
				GPIO.output(dac, decimal2binary(number))
				volt = float(number) / 256 * 3.3
				print(f"Volt: {volt:.4}")
			else:
				if number < 0:
					print("Your number less than 0!")
				elif number > 255:
					print("Your number more than 255!")
		except Exception:
			try:
				number = float(number)
			except ValueError:
				if number == "q":
					break
				print("Your symbols are not a number!")
				continue

			print("Your symbols are not a integer!")

finally:
	GPIO.output(dac, 0)
	GPIO.cleanup
