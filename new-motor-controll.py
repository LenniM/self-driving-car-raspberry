import RPi.GPIO as gpio
from time import sleep 
import time

motorOutput = 18

gpio.setmode(gpio.BCM)
gpio.setup(motorOutput, gpio.OUT)

time.sleep(1)

def set(property,value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, "w")
		f.write(value)
		f.close()
	except:
		print("Error while set " + property + " value: " + value)

p = gpio.PWM(motorOutput, 60)
p.start(18)#12

set("delayed", "0")
set("mode", "pwm")
set("frequency", "60")
set("active", "1")


time.sleep(1)
while True:
    inX = raw_input()
    if inX == "init":
        p.ChangeDutyCycle(9)
	print("init")
    if inX == "testTwo":
        print("meduium fast test")
        p.ChangeDutyCycle(10)
    if inX == "stop":
        gpio.cleanup()
        print("Stop test")
        break
