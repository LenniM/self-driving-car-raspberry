import time
import os
import platform
import sys
import threading
from .recording.image_training_recording import Record_Data_Linux
from .recording.image_training_recording import RecordingData
from multiprocessing import Process


motor = 14
servo = 23


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
            print(val)

            if(val == 27):
                print("Esc clicked")
                self.initial_motor_speed = 1500
                self.initial_servo_speed = 1500
                sys.exit()
            #W clicked
            elif(val == 119):
                if (self.isTriggered == True):
                    self.initial_motor_speed = 1500
                    self.isTriggered = False
                    print(self.initial_motor_speed)
                else:
                    self.initial_motor_speed = 1600
                    self.isTriggered = True
                    print(self.initial_motor_speed)
                print("w clicked")
            #S clicked
            elif(val == 115):
                print("Backwards movement not active")
                print("s clicked")  
                
            #D clicked
            elif(val == 100):
                if(self.initial_servo_speed < 1500):
                    self.initial_servo_speed = 1500
                    

                if(self.initial_servo_speed > 1500):
                    print("navigate backwards right")
                    if(self.initial_servo_speed < 2000):
                        self.initial_servo_speed += 50

                    maxRight = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxRight.start()
                    pass

                elif(self.initial_servo_speed >= 2000):
                    print("maximum right turn")

                else:
                    self.initial_servo_speed += 50
                    print(self.initial_servo_speed)


                print("d clicked")

            #a clicked
            elif(val == 97):

                if(self.initial_servo_speed > 1500):
                    self.initial_servo_speed = 1500
                    
                if(self.initial_servo_speed < 1500):
                    print("maximum backwards left")
                    if(self.initial_servo_speed > 1000):
                        self.initial_servo_speed -= 50  

                    maxLeft = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxLeft.start()
                    pass

                elif(self.initial_servo_speed <= 1000):
                    print("maximum left turn")

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

     

class MovementControllerLinux:

   

    
    #SERVO
    def turnIfNeed(self):
        self.isTriggeredTurn = True
        #right turn
        if(self.initial_servo_speed > 1500):
            while (self.initial_servo_speed > 1500):
                self.initial_servo_speed -= 25
                self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                print(self.initial_servo_speed)
                Record_Data_Linux(self.initial_servo_speed)
                time.sleep(0.3)
        elif(self.initial_servo_speed < 1500):
            while (self.initial_servo_speed < 1500):
                self.initial_servo_speed += 25
                self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                print(self.initial_servo_speed)
                Record_Data_Linux(self.initial_servo_speed)

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
                Record_Data_Linux(self.initial_servo_speed).stopRecording()
                sys.exit()

            #MOTOR
            #W clicked
            elif(val == 119):
              

                if (self.isTriggered == True):
                    self.initial_motor_speed = 1500
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    self.isTriggered = False
                    print(self.initial_motor_speed)
                    Record_Data_Linux(self.initial_servo_speed)

                else:
                    self.initial_motor_speed = 1600
                    self.pi.set_servo_pulsewidth(motor, self.initial_motor_speed)
                    self.isTriggered = True
                    print(self.initial_motor_speed)
                    Record_Data_Linux(self.initial_servo_speed)

                print("w clicked")
            #S clicked
            elif(val == 115):
                print("Backwards movement not active")
                print("s clicked")  
            
            #SERVO

            #D clicked
            elif(val == 100):
                if(self.initial_servo_speed < 1500):
                    self.initial_servo_speed = 1500
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    Record_Data_Linux(self.initial_servo_speed)


                if(self.initial_servo_speed > 1500):
                    print("navigate backwards right")
                    if(self.initial_servo_speed < 2000):
                        self.initial_servo_speed += 50
                        self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                        Record_Data_Linux(self.initial_servo_speed)

                    maxRight = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxRight.start()
                    pass

                elif(self.initial_servo_speed >= 2000):
                    print("maximum right turn")

                else:
                    self.initial_servo_speed += 50
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    print(self.initial_servo_speed)
                    Record_Data_Linux(self.initial_servo_speed)



                print("d clicked")

            #A clicked
            elif(val == 97):

                if(self.initial_servo_speed > 1500):
                    self.initial_servo_speed = 1500
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    Record_Data_Linux(self.initial_servo_speed)

                if(self.initial_servo_speed < 1500):
                    print("maximum backwards left")
                    if(self.initial_servo_speed > 1000):
                        self.initial_servo_speed -= 50  
                        self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                        Record_Data_Linux(self.initial_servo_speed)

                    maxLeft = threading.Thread(target=self.turnIfNeed)
                    if(self.isTriggeredTurn == False):
                        maxLeft.start()
                    pass

                elif(self.initial_servo_speed <= 1000):
                    print("maximum left turn")

                else:
                    self.initial_servo_speed -= 50
                    self.pi.set_servo_pulsewidth(servo, self.initial_servo_speed)
                    print(self.initial_servo_speed)
                    Record_Data_Linux(self.initial_servo_speed)

                print("a clicked")
            elif(val == 114):
		recordProcess = Process(target=RecordingData.startRecording)
		recordProcess.start()
		#startRecordingThread = threading.Thread(thread=Record_Data_Linux(self.initial_servo_speed).startRecording)
               	#startRecordingThread.start()
		#Record_Data_Linux(self.initial_servo_speed).startRecording
	 	#Record_Data_Linux(self.initial_servo_speed)

                print("r clicked")

            

    def __init__(self):

        self.pi = pigpio.pi()

        self.initial_servo_speed = 1500
        self.initial_motor_speed = 1500
        self.isTriggered = False
        self.isTriggeredTurn = False
        self.inputController()


class MovementControll:
    def __init__(self):
        if (platform.system() == "Linux"):
            MovementControllerLinux()
        elif(platform.system() == "Windows"):
            _MovementControllerWindows()
        else:
            print("not supported system")
   

    
      


if __name__ == '__main__':
    MovementControll()
