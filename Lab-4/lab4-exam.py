from sense_hat import SenseHat
from time import sleep
s = SenseHat()


# set a first inital boolean to know which letter is being showed
first_intial = False

s.clear()
while True:
  for event in s.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which letter
      if event.direction == "up":
        s.low_light == True # Show first intial 
      else if event.direction == "down":
        s.low_light == False
