from djitellopy import tello
import cv2
from keypress import getKey


me = tello.Tello()
me.connect()
print(me.get_battery()) #The battery of the drone

me.streamon() #open stream


while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240)) #reduce resolution to speed up the transmission of stream
    cv2.imshow("Image",img) #creat a window to show the stream signal
    cv2.waitKey(1)

