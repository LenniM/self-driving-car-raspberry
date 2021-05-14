import platform
import os



if(platform.system() == "Linux"):
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time
    import cv2

else:
    print("CANNOT IMPORT TRAINING DATA PACKAGES - NOT ON LINUX")

index = 0

class Record_Data_Linux(object):
    def __init__(self, current_servo_data):
        self.camera = PiCamera()
        self.rawCapture = PiRGBArray(self.camera)
        self.current_servo_data = current_servo_data

        if not os.path.exists(os.getcwd() + "/training-data-one"):
            os.makedirs(os.getcwd() + "/training-data-one")

    def record(self):
        servo_data = self.current_servo_data
        self.camera.capture(self.rawCapture, format="png")
        image = self.rawCapture.array

        img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)

        cv2.waitKey(0)
        index += 1
        


