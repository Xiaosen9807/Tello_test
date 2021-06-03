from socket import *
serverSocket=socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",8899))
serverSocket.listen(5)
clientSocket, clientInfo=serverSocket.accept()#accept()方法等待客户端连接
#clientSocket表示这个新客户端
#clientInfo表示这个新客户端的IP以及port
recvData=clientSocket.recv(1024)
print("%s:%s" % (str(clientInfo),recvData.decode('gb2312')))
clientSocket.close()
serverSocket.close()