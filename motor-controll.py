import RPi.GPIO as gpio
from time import sleep

motorOutput = 15

gpio.setmode(gpio.BCM)
gpio.setup(motorOutput, gpio.OUT)


gpio.output(motorOutput, gpio.LOW)

p = gpio.PWM(motorOutput, 1000)
p.start(25)

while True:
    inX = input()

    if inX == "test":
        GPIO.output(motorOutput,GPIO.HIGH)
        print("Fast test")
    if inX == "testTwo":
        print("meduium fast test")
        p.ChangeDutyCycle(50)
    if inX == "stop":
        GPIO.cleanup()
        print("Stop test")
        break