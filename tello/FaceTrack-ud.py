import cv2
import numpy as np
from djitellopy import tello
import time

try:
    me = tello.Tello()
    me.connect()
    print(me.get_battery())

    me.streamon()
    me.takeoff()
    me.send_rc_control(0, 0, 5, 0)
    time.sleep(2)

except:
    print('nodrones')

w, h = 360, 240
fbRange = [6200, 6800]
udRange = [-40, 40]
pid = [0.4, 0.4, 0]
xpError = 0
ypError = 0


def findFace(img):
    faceCascade = cv2.CascadeClassifier(
        r'D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
    )

    faces = faceCascade.detectMultiScale(img, 1.3, 5)

    myfacelistC = []
    myfacelistArea = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 2)
        #cv2.circle(img, (x, y), 8, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (180, 120), 8, (255, 255, 0), cv2.FILLED)

        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        cv2.line(img, (cx, cy), (180, 120), (0, 255, 255), 5)
        myfacelistC.append([cx, cy])
        myfacelistArea.append(area)
    if len(myfacelistArea) != 0:
        i = myfacelistArea.index(max(myfacelistArea))
        return img, [myfacelistC[i], myfacelistArea[i]]
    else:
        return img, [[0, 0], 0]


def trackFace(me, info, w, pid, xpError):
    area = info[1]
    x, y = info[0]
    uddistance = 240 - (y + h // 2)

    fb = 0
    ud = 0
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (
        error - xpError
    )  #speed sensetivity, if the error is too high, the speed used to change the angle is high correspondly
    speed = int(np.clip(speed, -100, 100))

    if udRange[0] < uddistance < udRange[1]:
        ud = 0
    if uddistance < udRange[0]:
        ud = -20
    elif uddistance > udRange[1] and uddistance != 120:
        ud = 20
    elif uddistance == 120:
        ud = 0

    area = info[1]
    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    if area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20

    if x == 0:
        speed = 0
        error = 0
        uddistance = 0

    #print(fb, ud, speed, '---', y, y + h // 2, uddistance)
    me.send_rc_control(0, fb, ud, speed)

    return error


#cap = cv2.VideoCapture(0)
while True:
    #ret, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    img, info = findFace(img)
    xpError = trackFace(me, info, w, pid, xpError)
    #print("Center:", info[0], "Area:", info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.streamoff()
        me.land()
        break
cv2.destroyAllWindows()
