from socket import *
server_socket=socket(AF_INET, SOCK_STREAM)
#绑定端口
server_socket.bind(("",8888))
#监听
server_socket.listen()
#等待客户端连接
client_socket, client_info=server_socket.accept()
while True:
    #接收消息
    recv_data=client_socket.recv(1024)
    print('客户端说：',recv_data.decode('utf-8'))
    #发送消息
    msg=input('>')
    client_socket.send(msg.encode('utf-8'))
    if msg=='bye':
        break
server_socket.close()
