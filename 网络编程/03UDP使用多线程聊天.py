from socket import *
from threading import Thread
udp_socket=socket(AF_INET, SOCK_DGRAM)
#绑定端口
udp_socket.bind(('',8989))

#不停接收
def recv_data():
    while True:
        recv_msg=udp_socket.recvfrom(1024)
        print(
            '>>%s:%s' % 
            (recv_msg[1],recv_msg[0].decode('gb2312'))
            )

#不停发送
def send_data():
    while True:
        data=input('<<:')
        addr=('192.168.0.104', 8080)
        udp_socket.sendto(data.encode('gb2312'),addr)
 
if __name__=='__main__':
    #创建两个线程
    t1=Thread(target=send_data)
    t2=Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()