#!/usr/bin/env python
#coding:utf8
import sys

def addr2dec(addr):
    items = [int(x) for x in addr.split('.')]
    return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])

def dec2addr(dec):
    return '.'.join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == 'addr':
            print addr2dec(sys.argv[2])
        elif sys.argv[1] == 'dec':
            print dec2addr(int(sys.argv[2]))
        else:
            print "Usage: %s [addr|dec] ip|num"
    else:
        print "Usage: %s [addr|dec] ip|num"
