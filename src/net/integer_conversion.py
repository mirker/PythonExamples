#!/usr/bin/env python

import socket

def convert_integer():
    data = 1234
    # 32 bits
    print "Orignal: %s => long host byte order: %s, Network byte order: %s" \
        %(data, socket.ntohl(data), socket.htonl(data))
    data2 = socket.ntohl(data)
    print data2, socket.htonl(data2)
    # 16 bits
    print "Orignal: %s => Short host byte order: %s, Network byte order: %s" \
        %(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()
