import socket
import time
import threading


class Tello:
    def _init_(self):
        self.local_ip=''
        self.local_port=8080
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.local_ip, self.local_port)

        #Thread for receive cmd ack
        self.receive_thread = threading.Thread(target=self.receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        
        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log=[]

        self.MAX_TIME_OUT=15.0
    

    def send_command(self, command):
        
        self.log.append(command)

        self.socket.sendto(command.encode('utf-8'),self.tello_address)
        print('sending command: %s to %s' % (command, self.tello_ip))
        
        Start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - Start
            if diff > self.MAX_TIME_OUT:
                print ('Max timeout exceeded.... command:', command)
                return
        print('Done!!! send command: %s to %s' % (command, self.tello_ip))

    
    def _recevied_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print ('from %s: %s', (ip,self.response))

                self.log[-1].add_response(self.response)
            except:
                print ('Caught exception socket.error')
    

    def on_close(self):
        pass


    def get_log(self):
        return self.log