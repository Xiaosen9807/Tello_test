from socket import *
s=socket(AF_INET, SOCK_DGRAM)#创建套接字
addr=('192.168.0.104',8080)#准备接收方地址
data=input("请输入：")
s.sendto(data.encode('gb2312'),addr)
s.close() 