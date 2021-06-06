from socket import *
from threading import Thread
import keypress as kp
tello_socket=socket(AF_INET, SOCK_DGRAM)
#绑定端口
tello_socket.bind(('',8080))

#不停接收
def recv_data():
    while True:
        recv_msg=tello_socket.recvfrom(1024)
        print(
            '>>%s:%s' % 
            (recv_msg[1],recv_msg[0].decode('utf-8'))
            )

#不停发送
def send_data():
    Commandmodule = 'command'
    addr=('192.168.10.1', 8889)
    tello_socket.sendto(Commandmodule.encode('utf-8'),addr)
    while True:
        data=input('')
        addr=('192.168.10.1', 8889)
        tello_socket.sendto(data.encode('utf-8'),addr)
        
        if data == 'end':
            print ('...')
            tello_socket.close()  
            break
 
if __name__=='__main__':
    #创建两个线程
    t1=Thread(target=send_data)
    t2=Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()