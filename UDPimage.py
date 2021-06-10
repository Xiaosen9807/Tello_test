from socket import *
import threading
import cv2
import numpy as np
import imageio

tello_socket = socket(AF_INET, SOCK_DGRAM)
video_socket = socket(AF_INET, SOCK_DGRAM)
#绑定端口
tello_socket.bind(('', 8080))
video_socket.bind(('', 11111))


#不停接收
def recv_data():
    while True:
        recv_msg = tello_socket.recvfrom(1024)
        print('>>%s:%s' % (recv_msg[1], recv_msg[0].decode('utf-8')))


#不停发送
def send_data():
    Commandmodule = 'command'
    addr = ('192.168.10.1', 8889)
    tello_socket.sendto(Commandmodule.encode('utf-8'), addr)
    while True:
        data = input('')
        addr = ('192.168.10.1', 8889)
        tello_socket.sendto(data.encode('utf-8'), addr)


#接收视频


def recv_stream():
    while True:
        recvData,addr = video_socket.recvfrom(400000)
        

      
        recvData = np.frombuffer(recvData, dtype=np.uint8)
        print(recvData)

        if recvData[0]:
            imde = cv2.imdecode(recvData, 1)
            print(imde,'1')
            print("imshow........")
            cv2.imshow('img', imde)
            cv2.waitKey(1)

        #except:
            #print('video identificated error')
    # recv_video = np.array(recv_video, dtype=np.uint8)
    # if recv_video:
    #recv_video = cv2.resize(recv_video, (360, 240))

    #cv2.imshow("Image", recv_video)  #creat a window to show the stream signal
    #cv2.waitKey(1)


if __name__ == '__main__':
    #创建两个线程
    t1 = threading.Thread(target=send_data)
    t1.daemon = True
    t2 = threading.Thread(target=recv_data)
    t2.daemon = True
    t3 = threading.Thread(target=recv_stream)
    t3.daemon = True
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join