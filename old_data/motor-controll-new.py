import os
import time
os.system("sudo pigpiod")
time.sleep(1)
import pigpio

pi = pigpio.pi()

ESC = 18

pi.set_servo_pulsewidth(ESC, 0)



max_value = 2000
min_value = 700

while True:

    inX = raw_input()

    if inX == ("test"):
        print("low speed")
        pi.set_servo_pulsewidth(ESC, min_value)
    if inX == ("fast"):
        print("fast speed")
        pi.set_servo_pulsewidth(ESC, max_value)

    if inX == ("stop"):
        pi.set_servo_pulsewidth(ESC, 0)
        pi.stop()
        break

