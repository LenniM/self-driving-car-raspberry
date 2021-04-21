import RPi.GPIO as gpio
import time

servo = 14
gpio.setmode(gpio.BCM)
gpio.setup(servo, gpio.OUT)

p = gpio.PWM(servo, 50)
p.start(2.5)
try:
  while True:
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
except KeyboardInterrupt:
  p.stop()
