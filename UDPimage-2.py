from socket import *
import threading
import cv2
import numpy as np
from time import sleep

tello_socket = socket(AF_INET, SOCK_DGRAM)
video_socket = socket(AF_INET, SOCK_DGRAM)
#绑定端口
tello_socket.bind(('', 8080))
#video_socket.bind(('', 11111))


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
    tello_ip = '0.0.0.0'
    while True:
        try:
            recv_video = cv2.VideoCapture('udp://' + tello_ip + ':11111')
            print(recv_video)
            print('||||||||||||||||')
        except:
            print('x')
            print('-----------------')
            print(recv_video)
      
            sleep(3)
            break

        try:
            while True:
                ret, video_signal = recv_video.read()
                video_signal = cv2.resize(video_signal, (360, 240))
                cv2.imshow('streamsignal', video_signal)
                if cv2.waitKey(10):
                    break
        except:
            print('y')
            print('------------------')
            print(video_signal)
            break
    recv_video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #创建三个线程
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