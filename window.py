#!C:\Python27\python.exe
# -*- coding:UTF-8 -*-
import socket
import time
import sys
from Tkinter import *

def center_window(w = 300, h = 300):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def udp(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (ip, int(port))       #服务器端地址
    try:
        while True:
            data = 'hello world\n'
            s.sendto(data.encode(), addr)    #发送到服务端
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        s.close()


def addr2dec(addr, e):
    if addr:
        if len(addr.split('.')) == 4:
            items = [int(x) for x in addr.split('.')]
            result = sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])
            e.set(result)

def dec2addr(dec):
    return '.'.join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])

if __name__ == '__main__':
    root = Tk(className='python tool')
    center_window(500, 300)
    Label(root, text="addr TO dec").grid(row=0)
    add_dec_b1 = Button(root, text="change", command=lambda: addr2dec(add_dec_e1.get(), e2))
    add_dec_e1 = Entry(root)
    e2 = StringVar()
    add_dec_e2 = Entry(root, textvariable = e2)
    e2.set("")
    add_dec_e1.grid(row=0, column=1)
    add_dec_b1.grid(row=0, column=2)
    add_dec_e2.grid(row=0, column=3)
    root.mainloop()
