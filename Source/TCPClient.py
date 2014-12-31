'''
Created on Dec 31, 2014

@author: PayneMoM

Chapter 2
Black Hat Python 
'''


import socket

target_host = '127.0.0.1'
target_port = 9999

def main():
    
    #Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Connect the client
    client.connect((target_host,target_port))

    #Send some data
    #client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\n")
    client.send("Love you Beautiful!")
    
    #receive some data
    response = client.recv(4096)
    
    print response
    
if __name__ == '__main__':
    main()