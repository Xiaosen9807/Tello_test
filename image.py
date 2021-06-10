from djitellopy import tello
import cv2
import keypress as kp


me = tello.Tello()
me.connect()
print(me.get_battery()) #The battery of the drone

me.streamon() #open stream


def getKeyboardInput():

    if kp.getKey("x"): me.streamoff()
    elif kp.getKey("c"): me.streamon()


while True:
    Values=getKeyboardInput()
    me.send_rc_control(Values)
    img = me.get_frame_read().frame
    print(type(img))
    img = cv2.resize(img, (360,240)) #reduce resolution to speed up the transmission of stream
    cv2.imshow("Image",img) #creat a window to show the stream signal
    cv2.waitKey(1)
