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
      if first_intial == False:
        s.show_letter("A") # Show first intial
        first_intial = True 
      else:
        s.show_letter("A") # Show Last intial
        first_intial = False 

      # Wait a while and then clear the screen
      sleep(0.5)
      s.clear()