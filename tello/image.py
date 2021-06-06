from djitellopy import tello
import cv2
import pygame


me = tello.Tello()
me.connect()
print(me.get_battery()) #The battery of the drone

me.streamon() #open stream

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False 
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def getKeyboardInput():

    if getKey("x"): me.streamoff()
    elif getKey("c"): me.streamon()

while True:
    Values=getKeyboardInput()
    me.send_rc_control(Values)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240)) #reduce resolution to speed up the transmission of stream
    cv2.imshow("Image",img) #creat a window to show the stream signal
    cv2.waitKey(1)

