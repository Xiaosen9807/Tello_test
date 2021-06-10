from djitellopy import tello
import keypress as kp
from time import sleep


kp.init()
me=tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed
    
    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("l"): me.land(), print('Land!')
    elif kp.getKey("RETURN"): me.takeoff(), print('Take Off!')
    
    
    return [lr, fb, ud, yv]



#me.takeoff()
#me.land()


while True:
    values=getKeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.05)