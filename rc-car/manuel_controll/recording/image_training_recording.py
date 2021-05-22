import platform
import os
import io


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
        
        with picamera.PiCamera() as camera:
    # Set the camera's resolution to VGA @40fps and give it a couple
    # of seconds to measure exposure etc.
            camera.resolution = (1280, 720)
            camera.framerate = 80
            time.sleep(2)
            # Set up 40 in-memory streams
            outputs = [io.BytesIO() for i in range(40)]
            start = time.time()
            image = camera.capture_sequence(outputs, 'jpeg', use_video_port=True)
            img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
            cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
            cv2.waitKey(0)
            finish = time.time()
        
      # with self.camera as camera:
        #    with picamera.array.PiRGBArray(camera) as output:
         #       camera.resolution = (1280, 720)
           #     camera.capture(output, 'png')
          #      image = output.rawCapture.array
            #    img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
             #   cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
              #  cv2.waitKey(0)
               # index += 1
                #stream.truncate(0)  
        #with self.camera as camera:
       #     stream = io.BytesIO()
      #      for x in camera.capture_continuous(stream, format="png"):
                
     #           img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
    #            cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
 ##               cv2.waitKey(0)
   #             index += 1
#
   #             stream.truncate()
  #              stream.seek(0)
 #               if process(stream):
#                       break
      #  self.camera.capture(self.rawCapture, format="png")
       # image = self.rawCapture.array

      #  img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
     #   cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)

        cv2.waitKey(0)
        index += 1
        


