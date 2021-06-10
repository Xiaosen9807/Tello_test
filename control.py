from djitellopy import tello
from time import sleep #Add some pause in the program




me=tello.Tello()
me.connect()
print(me.get_battery()) #The battery of the drone

me.takeoff
me.send_rc_control(0,0,0,0)
sleep(2)
me.land()
