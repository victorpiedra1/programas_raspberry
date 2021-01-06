from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/Videos/video.h264')
sleep(3600)
camera.stop_recording()
camera.stop_preview()
   

    
