import picamera
from time import sleep

# A script that sets up the picamera and shows a 20 seconds preview, 
# this would be later on implemented in the GUI part of the project.

with picamera.PiCamera() as camera:
    camera.resolution = (1280,720) # Setting the camera resolution to 720p
    camera.start_preview(alpha=192) # Starting camera preview
    sleep(20) 
    camera.stop_preview() # Stops camera preview after 20 seceonds 