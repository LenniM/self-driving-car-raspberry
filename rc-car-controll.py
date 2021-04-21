import time
import os
import platform
import sys
import threading
import pigpio

motor = 14
servo = 23

pi = pigpio.pi()

pi.set_servo_pulsewidth(motor, 1500)
time.sleep(1)
pi.set_servo_pulsewidth(motor, 1500)

if (platform.system() ==  "Linux"):
    import pigpio

    pi = pigpio.pi()

    pi.set_servo_pulsewidth(motor, 1500)
    time.sleep(1)

    pi.set_servo_pulsewidth(motor, 1500)
else:
    print("Not on Linux")
print("motor started")


#Input getter
class _Getch:

   def __init__(self):
         try:
            self.impl = _GetchWindows()
         except ImportError:
            try:
               self.impl = _GetchUnix()
            except:
               print("error while init (getch)")

   def __call__(self): 
      return self.impl()

class _GetchWindows:
   def __init__(self):
      import msvcrt

   def __call__(self):
      import msvcrt
      return msvcrt.getch()

class _GetchUnix:
    def __init__(self):
        import tty, sys, termios 

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		
        return ch




#Controller

class _MovementControllerWindows:

    def slowDownIfNeed(self):
        self.isTriggered = True
        time.sleep(2) 
        #forward
        if(self.initial_motor_speed > 1500):   
            while (self.initial_motor_speed > 1500):

                self.initial_motor_speed -= 15
                print(self.initial_motor_speed)
                time.sleep(0.5)
        #backwards
        elif(self.initial_motor_speed < 1500):
             while (self.initial_motor_speed < 1500):
                self.initial_motor_speed += 15
                print(self.initial_motor_speed)
                time.sleep(0.5)
        self.isTriggered = False
    
    def turnIfNeed(self):
        self.isTriggeredTurn = True
        #right turn
        if(self.initial_servo_speed > 1500):
            while (self.initial_servo_speed > 1500):
                self.initial_servo_speed -= 25
                print(self.initial_servo_speed)
                time.sleep(0.3)
        elif(self.initial_servo_speed < 1500):
            while (self.initial_servo_speed < 1500):
                self.initial_servo_speed += 25
                print(self.initial_servo_speed)
                time.sleep(0.3)
        self.isTriggeredTurn = False



    def inputController(self):
         while True:
            inkey = _Getch()
            while(1):
                k = inkey()
                if k!= '':break

            val = ord(k)

            if(val == 27):
                print("Esc clicked")
                self.initial_motor_speed = 1500
                self.initial_servo_speed = 1500
                sys.exit()
            #W clicked
            elif(val == 119):
                if(self.initial_motor_speed < 1500):
                    self.initial_motor_speed = 1500
                    time.sleep(0.4)
                #If motorspeed is above maximum
                if(self.initial_motor_speed >= 1750):
                    print("maximum forward speed")
                    maxForward = threading.Thread(target=self.slowDownIfNeed)
                    if(self.isTriggered == False):
                        maxForward.start()
                    pass
                #If motorspeed is not above maximum
                else:
                    self.initial_motor_speed += 15
                    print(self.initial_motor_speed)

                print("w clicked")
            #S clicked
            elif(val == 115):
                if(self.initial_motor_speed > 1500):
                    self.initial_motor_speed = 1500
                    time.sleep(0.4)

                #If motorspeed is below minimum
                if(self.initial_motor_speed <= 1250):
                    maxBackwards = threading.Thread(target=self.slowDownIfNeed)

                    if(self.isTriggered == False):
                        maxBackwards.start()
                    pass
                    print("minimum backward speed")
                #If motorspeed is above minimum
                else:
                    self.initial_motor_speed -= 15
                    print(self.initial_motor_speed)
                print("s clicked")  
            #D clicked
            elif(val == 100):
                if(self.initial_servo_speed < 1500):
                    self.initial_servo_speed = 1500
                    

                if(self.initial_servo_speed >= 1900):
                    print("maximum right turn")
                    maxRight = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxRight.start()
                    pass
                else:
                    self.initial_servo_speed += 50
                    print(self.initial_servo_speed)


                print("d clicked")

            elif(val == 97):

                if(self.initial_servo_speed > 1500):
                    self.initial_servo_speed = 1500
                    
                if(self.initial_servo_speed <= 1250):
                    print("maximum left turn")
                    maxLeft = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxLeft.start()
                    pass
                else:
                    self.initial_servo_speed -= 50
                    print(self.initial_servo_speed)
                print("a clicked")

    def __init__(self):
        self.initial_servo_speed = 1500
        self.initial_motor_speed = 1500
        self.isTriggered = False
        self.isTriggeredTurn = False
        self.inputController()

     

class _MovementControllerLinux:

    #MOTOR
    def slowDownIfNeed(self):
        self.isTriggered = True
        time.sleep(2) 
        #forward
        if(self.initial_motor_speed > 1500):   
            while (self.initial_motor_speed > 1500):

                self.initial_motor_speed -= 20
                self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                print(self.initial_motor_speed)
                time.sleep(0.5)
        #backwards
        elif(self.initial_motor_speed < 1500):
             while (self.initial_motor_speed < 1500):
                self.initial_motor_speed += 20
                self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                print(self.initial_motor_speed)
                time.sleep(0.5)
        self.isTriggered = False
    
    #SERVO
    def turnIfNeed(self):
        self.isTriggeredTurn = True
        #right turn
        if(self.initial_servo_speed > 1500):
            while (self.initial_servo_speed > 1500):
                self.initial_servo_speed -= 25
                self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                print(self.initial_servo_speed)
                time.sleep(0.3)
        elif(self.initial_servo_speed < 1500):
            while (self.initial_servo_speed < 1500):
                self.initial_servo_speed += 25
                self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                print(self.initial_servo_speed)
                time.sleep(0.3)
        self.isTriggeredTurn = False



    def inputController(self):
         while True:
            inkey = _Getch()
            while(1):
                k = inkey()
                if k!= '':break

            val = ord(k)

            if(val == 27):
                print("Esc clicked")
                self.initial_motor_speed = 1500
                self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                self.initial_servo_speed = 1500
                self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                sys.exit()

            #MOTOR
            #W clicked
            elif(val == 119):
                if(self.initial_motor_speed < 1500):
                    self.initial_motor_speed = 1500
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    time.sleep(0.4)
                #If motorspeed is above maximum
                if(self.initial_motor_speed >= 1600):
                    print("maximum forward speed")
                    maxForward = threading.Thread(target=self.slowDownIfNeed)
                    if(self.isTriggered == False):
                        maxForward.start()
                    pass
                #If motorspeed is not above maximum
                else:
                    self.initial_motor_speed += 25
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    print(self.initial_motor_speed)

                print("w clicked")
            #S clicked
            elif(val == 115):
                if(self.initial_motor_speed > 1500):
                    self.initial_motor_speed = 1500
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    time.sleep(0.7)
		    self.pi.set_servo_pulsewidth(motor, 1400)
		    time.sleep(0.3)
                #If motorspeed is below minimum
                if(self.initial_motor_speed <= 1350):
                    maxBackwards = threading.Thread(target=self.slowDownIfNeed)

                    if(self.isTriggered == False):
                        maxBackwards.start()
                    pass
                    print("minimum backward speed")
                #If motorspeed is above minimum
                else:
                    self.initial_motor_speed -= 25
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    print(self.initial_motor_speed)
                print("s clicked")  
            
            #SERVO

            #D clicked
            elif(val == 100):
                if(self.initial_servo_speed < 1500):
                    self.initial_servo_speed = 1500
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    

                if(self.initial_servo_speed >= 1900):
                    print("maximum right turn")
                    maxRight = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxRight.start()
                    pass
                else:
                    self.initial_servo_speed += 50
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    print(self.initial_servo_speed)


                print("d clicked")
            #A clicked
            elif(val == 97):

                if(self.initial_servo_speed > 1500):
                    self.initial_servo_speed = 1500
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)

                    
                if(self.initial_servo_speed <= 1100):
                    print("maximum left turn")
                    maxLeft = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxLeft.start()
                    pass
                else:
                    self.initial_servo_speed -= 50
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    print(self.initial_servo_speed)
                print("a clicked")

    def __init__(self):

        self.pi = pigpio.pi()

        self.initial_servo_speed = 1500
        self.initial_motor_speed = 1500
        self.isTriggered = False
        self.isTriggeredTurn = False
        self.inputController()


class _MovementControll:
    def __init__(self):
        if (platform.system() == "Linux"):
            _MovementControllerLinux()
        elif(platform.system() == "Windows"):
            _MovementControllerWindows()
        else:
            print("not supported system")
   

    
      


if __name__ == '__main__':
    _MovementControll()
