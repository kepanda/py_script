#!/usr/bin/env python
#coding:utf8
import socket
import time
import sys
if len(sys.argv) != 3:
    print "Usage: %s 10.10.10.10 10020" % sys.argv[0]
    sys.exit(1)
ip = sys.argv[1]
port = sys.argv[2]

def udp(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     
    addr = (ip, int(port))       #服务器端地址
    
    try:
        while True:
            data = 'hello world\n'
            s.sendto(data.encode(), addr)    #发送到服务端
            time.sleep(1)
            #data = input('请输入要处理的数据:') #获得数据
            #if not data or data == 'quit':
            #    break
            #s.sendto(data.encode(), addr)    #发送到服务端
            #recvdata, addr = s.recvfrom(1024)  #接收服务器端发来的数据
            #print(recvdata.decode('utf-8'))    #解码打印
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        s.close()
if __name__ == '__main__':
    udp(ip, port)
