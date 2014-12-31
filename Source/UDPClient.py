'''
Created on Dec 31, 2014

@author: PayneMoM
Chapter 2
Black Hat Python 
'''

import socket

target_host = '127.0.0.1'
target_port = 80

def main():
    
    #Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Send some data
    client.sendto("Love you Babe!", (target_host,target_port))
    
    
    #receive some data
    data, addr = client.recvfrom(4096)
    
    print data
    
if __name__ == '__main__':
    main()