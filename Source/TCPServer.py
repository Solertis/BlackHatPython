'''
Created on Dec 31, 2014

@author: PayneMoM
Chapter 2
Black Hat Python 
'''
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print "[+] Listening on %s:%d" % (bind_ip,bind_port)

#This is our client handling thread
def handle_client(client_sock):
    
    #print out what the client sends
    request = client_sock.recv(1024)
    print "[*] Received: %s" % request

    #Send back a packet
    client_sock.send("ACK!")
    
    #Close the sock
    client_sock.close()
    



    
while True:
    
    client, addr = server.accept()
    
    print "[+] Accepted connection from: %s:%d" % (addr[0], addr[1])
    
    #Spin up our client handler to handle incoming data
    
    client_handler = threading.Thread(target= handle_client,args=(client,))
    client_handler.start()
    
