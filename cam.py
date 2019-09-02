from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (600, 400)

camera.start_preview()
#camera.start_recording('/home/pi/Desktop/video.h264')
sleep(150)
#camera.stop_recording()
camera.stop_preview()
