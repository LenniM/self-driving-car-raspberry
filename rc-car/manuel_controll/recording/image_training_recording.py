import platform
import os
import io
import threading
import numpy as np

if(platform.system() == "Linux"):
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import picamera
    import time
    import cv2

else:
    print("CANNOT IMPORT TRAINING DATA PACKAGES - NOT ON LINUX")


class Record_Data_Linux(object):
    def __init__(self, current_servo_data):
        # self.camera = PiCamera()
        # self.rawCapture = PiRGBArray(self.camera)
        self.current_servo_data = current_servo_data
        self.shouldStop = False
        self.shouldStart = False
        self.index = 0
       # self.camera = None
        if not os.path.exists(os.getcwd() + "/training-data-one"):
            os.makedirs(os.getcwd() + "/training-data-one")
        self.startRecording
            
    def onServoDataChanged(self):
        pass

    def stopRecording(self):
        self.shouldStop = True
    
    def videoCapture(self):
        while self.shouldStop == False:
            self.camera.capture(os.getcwd() + "/training-data-one/" + "training-data-one" + "-" + str(self.index) + "-" + str(self.current_servo_data) + ".png")
            self.index += 1

    def startRecording(self):
        self.shouldStart = True
        if self.shouldStart == True and self.shouldStop == False:
          #  startVideoCapture = threading.Thread(target=self.videoCapture) 
            with picamera.PiCamera() as camera:
                camera.resolution = (1280, 720)
                camera.rotation = 180
                camera.framerate = 60
               # startVideoCapture.start()
               # while self.shouldStop == False:
                camera.capture(os.getcwd() + "/training-data-one/" + "training-data-one" + "-" + str(self.index) + "-" + str(self.current_servo_data) + ".png")
                self.index += 1
                #outputs = [io.BytesIO() for i in range(40)]
          #      stream = io.BytesIO()
               # camera.capture_sequence(os.getcwd() + "/training-data-one/" + "training-data-one" + "-" + str(self.index) + "-" + outputs + "-" + str(self.current_servo_data) + ".jpg", use_video_port=True)
           #     camera.capture_sequence(stream, "jpeg", use_video_port=True)
                
            #    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                
             #   img = cv2.decode(data, 1)
                
              #  cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",self.index,self.current_servo_data), img)
                
               # self.index += 1

             #   if(self.shouldStop == True):
              #      break
           # with picamera.PiCamera() as camera:
            #    camera.resolution = (1280, 720)
             #   camera.rotation = 180
              #  time.sleep(0.5)
              #  print("camera started")
               # automatic_name = (os.getcwd() + "/training-data-one/", "%s_%03d_%03d.jpg" % ("training-data-one",self.index,self.current_servo_data))
              #  for i, filename in enumerate(camera.capture_continuous(os.getcwd() + "/training-data-one/" + "training-data-one" + "-" + str(self.index) + "-" + str(self.current_servo_data) + ".jpg")):
               #     print(i)
                #    self.index += 1
#
  #                  if(self.shouldStop == True):
 #                       break



    # def record(self):
    #     if self.shouldStart == True:
    #         with picamera.PiCamera() as camera:
    #             camera.resolution = (1280, 720)
    #             camera.rotation = 180
    #             time.sleep(0.5)
    #             print("camera started")

    #             for i, filename in enumerate(camera.capture_continuous(os.getcwd() + "/training-data-one/", "%s_%03d_%03d.jpg" % ("training-data-one",index,self.current_servo_data))):
    #                 print(i)
    #                 index += 1

    #                 if(self.shouldStop == True):
    #                     break


 


                            # maxRight = threading.Thread(target=self.turnIfNeed)
        






# class Record_Data_Linux(object):
#     def __init__(self, current_servo_data):
#         self.camera = PiCamera()
#         self.rawCapture = PiRGBArray(self.camera)
#         self.current_servo_data = current_servo_data

#         if not os.path.exists(os.getcwd() + "/training-data-one"):
#             os.makedirs(os.getcwd() + "/training-data-one")

#     def record(self):
#         servo_data = self.current_servo_data
        
#         with picamera.PiCamera() as camera:
#     # Set the camera's resolution to VGA @40fps and give it a couple
#     # of seconds to measure exposure etc.
#             camera.resolution = (1280, 720)
#             camera.framerate = 80
#             time.sleep(2)
#             # Set up 40 in-memory streams
#             outputs = [io.BytesIO() for i in range(1)]
#             start = time.time()
#             camera.capture_sequence(outputs, 'png', use_video_port=True)
#             img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
#             cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
#             cv2.waitKey(0)
#             finish = time.time()
        
#       # with self.camera as camera:
#         #    with picamera.array.PiRGBArray(camera) as output:
#          #       camera.resolution = (1280, 720)
#            #     camera.capture(output, 'png')
#           #      image = output.rawCapture.array
#             #    img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
#              #   cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
#               #  cv2.waitKey(0)
#                # index += 1
#                 #stream.truncate(0)  
#         #with self.camera as camera:
#        #     stream = io.BytesIO()
#       #      for x in camera.capture_continuous(stream, format="png"):
                
#      #           img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
#     #            cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)
#  ##               cv2.waitKey(0)
#    #             index += 1
# #
#    #             stream.truncate()
#   #              stream.seek(0)
#  #               if process(stream):
# #                       break
#       #  self.camera.capture(self.rawCapture, format="png")
#        # image = self.rawCapture.array

#       #  img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
#      #   cv2.imwrite(os.getcwd() + "/training-data-one", "%s_%03d_%03d.jpg" % ("training-data-one",index,servo_data), img_rotate_180)

#         cv2.waitKey(0)
#         index += 1
        


