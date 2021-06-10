from djitellopy import tello
import keypress as kp
import time
import cv2
global img

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()  #open stream


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("l"): me.land()
    elif kp.getKey("RETURN"): me.takeoff()

    if kp.getKey("x"): me.streamoff()
    elif kp.getKey("c"): me.streamon()

    if kp.getKey("z"):
        cv2.imwrite(f'C:/Users/Surface/Desktop/images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


#me.takeoff()

while True:
    values = getKeyboardInput()
    me.send_rc_control(values[0], values[1], values[2], values[3])
    img = me.get_frame_read().frame
    print(img)
    img = cv2.resize(
        img,
        (360, 240))  #reduce resolution to speed up the transmission of stream
    cv2.imshow("Image", img)  #creat a window to show the stream signal
    cv2.waitKey(1)
