from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array


img_rotate_180 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imwrite("rotatedimage.jpg", img_rotate_180)

cv2.waitKey(0)
