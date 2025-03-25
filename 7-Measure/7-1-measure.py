import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)
leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.HIGH)

comp = 14
troyka = 13
sleeping = 0.005
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    val = 128
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 128

    val += 64
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 64

    val += 32
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 32

    val += 16
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 16

    val += 8
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 8

    val += 4
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 4

    val += 2
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 2

    val += 1
    GPIO.output(dac, [int (elem) for elem in bin(val)[2:].zfill(8)])
    time.sleep(sleeping)
    if (GPIO.input(comp)):
        val -= 1

    return val

data_value = []

try:
    volt = 0
    count = 0

    print('Condensator starts charging')
    time_start = time.time()
    while volt < (255 / 100 * 81):
        volt = adc()
        data_value.append(volt)
        time.sleep(0.0005)
        count += 1
        GPIO.output(leds, [int (elem) for elem in bin(volt)[2:].zfill(8)])
    GPIO.setup(troyka,GPIO.OUT, initial = GPIO.LOW)

    print('Condensator starts discharging')
    while volt > (255 / 100 * 70):
        volt = adc()
        data_value.append(volt)
        time.sleep(0.0005)
        count += 1
        GPIO.output(leds, [int (elem) for elem in bin(volt)[2:].zfill(8)])
    time_experiment = time.time()
    time_experiment -= time_start

    print('Writing to file')
    with open('data.txt', 'w') as f:
        for value in data_value:
            f.write(str(value) + '\n')

    with open('settings.txt', 'w') as f:
        f.write(str(count / time_experiment) + '\n')
        f.write('0.5')

    print('Time of experiment: {}'.format(time_experiment))
    print('Time of one measurement: {}'.format(time_experiment / count))
    print('Average sampling rate: {}'.format(count / time_experiment))
    print('ADC Quant step {}'.format(0.5))

    print('Graphs')
    y = [i / 255 * 3.3 for i in data_value]
    x = [i * time_experiment / count for i in range(count)]
    pyplot.plot(x, y)
    pyplot.xlabel('Time')
    pyplot.ylabel('Volt')
    pyplot.show()

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()
