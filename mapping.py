from djitellopy import tello
import keypress as kp
from time import sleep
import numpy as np
import cv2
import math



#####Parameters#####
fSpeed = 117/10 #Forward Speed in cm/s (15cm/s)
aSpeed = 360/10 #Angular Speed Degree/s (50d/s)
interval = 0.25


dInterval = fSpeed*interval
aInterval = aSpeed*interval
####################
x, y = 500, 500
a = 0
yaw = 0


kp.init()
me=tello.Tello()
me.connect()
print(me.get_battery())


points = [(0, 0), (0, 0)]


def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 15
    aSpeed = 50
    d = 0
    global x, y, yaw, a

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"): 
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"): 
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"): 
        ud = speed

    elif kp.getKey("s"): 
        ud = -speed

    if kp.getKey("a"): 
        yv = aSpeed
        yaw -= aInterval

    elif kp.getKey("d"): 
        yv = -aSpeed
        yaw += aInterval

    if kp.getKey("l"): me.land(), print('Land!'); sleep(3)
    elif kp.getKey("RETURN"): me.takeoff(), print('Take Off!')
    
    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))
    
    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 5, (0, 0, 255), cv2.FILLED) #Blue, Green, Red
    cv2.circle(img, (point[0], point[1]), 8, (0, 225, 0), cv2.FILLED) #Blue, Green, Red
    cv2.putText(
        img, f'({(points[-1][0]- 500)/100}, {(points[-1][1]- 500)/100})m',
        (points[-1][0] + 10, points[-1][1] + 30),
        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1  
    )    

while True:
    values=getKeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if (points[-1][0] != values[4] or points[-1][1] != values[5]):
        points.append((values[4], values[5]))
    drawPoints(img, points)
    cv2.imshow("OutPut", img)
    cv2.waitKey(1)