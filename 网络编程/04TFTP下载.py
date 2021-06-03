import struct
from socket import *
file_name="1234.txt"
sever_ip='127.0.0.1'
send_data=struct.pack(
    '!H%dsb5sb' % len(file_name),1,file_name.encode(),0,'octet'.encode(),0
)
s=socket(AF_INET, SOCK_DGRAM)
s.sendto(send_data,(sever_ip,69))#第一次发送，连接服务器69端口
f=open(file_name,'ab')#a：以追加模式打开（必要时可安装）append；b：二进制
while True:
    recv_data=s.recvfrom(1024)#接收数据
    caozuoma,ack_num=struct.unpack('!HH',recv_data[0][:4])#获取数据块编号
    rand_port=recv_data[1][1]#获取服务器随机端口
    if int(caozuoma)==5:
        print('文件不存在...')
        break
    print(
        "操作码：%d，ACK：%d，服务器随机端口：%d，数据长度：%d" 
        %
        (caozuoma,ack_num,rand_port,len(recv_data[0]))
    )
    f.write(recv_data[0][4:])#写入数据
    if len(recv_data[0])<516:
        break
    ack_data=struct.pack("!HH",4,ack_num)
    s.sendto(ack_data,(sever_ip,rand_port))#回复ACK确认包
