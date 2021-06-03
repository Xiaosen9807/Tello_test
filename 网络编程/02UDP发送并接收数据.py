from socket import *
s=socket(AF_INET, SOCK_DGRAM)#创建套接字
s.bind(('',8890))#绑定一个端口，ip地址和端口号，IP地址可以不写

addr=('192.168.0.104',8080)#准备接收方地址
data=input("请输入：")
s.sendto(data.encode('gb2312'),addr)
redata=s.recvfrom(1024)#接收数据最大字节数为1024
print(redata)
print('接收到%s的消息%s' % (redata[1],redata[0].decode('gb2312')))
s.close() 