import RPi.GPIO as gpio
from time import sleep
import time

motorOutput = 18

gpio.setmode(gpio.BCM)
gpio.setup(motorOutput, gpio.OUT)


p = gpio.PWM(motorOutput, 60)
p.start(0)

time.sleep(1)
while True:
    inX = raw_input()
    if inX == "init":
	for i in range(100):
		p.ChangeDutyCycle(i)
		time.sleep(1)
	for i in range(100,0):
		p.ChangeDutyCycle(i)
		time.sleep(1)
        p.ChangeDutyCycle(9)
	print("init")
	inX = "0"
    if inX == "testTwo":
        print("meduium fast test")
        p.ChangeDutyCycle(10)
    if inX == "stop":
	p.stop()
        gpio.cleanup()
        print("Stop test")
        break
