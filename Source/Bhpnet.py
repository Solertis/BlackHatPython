'''
Created on Dec 31, 2014

@author: PayneMoM
Chapter 2
Black Hat Python 
'''
import sys, socket, getopt, threading, subprocess
from test.test_itertools import errfunc


#Define global variables

listen=False
command=False
upload=False
execute=""
target=""
upload_destination=""
port=0

#Responsible for handing command line arguments and calling the rest of the functions
def usage():
    print "BHP Net Tool"
    print
    print "Usage bhpney.py -t target_host -p port"
    print "-l --listen                 -listen on [host]:[port] for incoming connections"
    print 
    print "-e --execute=file_to_run    -Execute the given file upon receiving connection"
    print "-c --command                -Initialize a command shell"
    print
    print
    print "-u --upload=destination     -upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "Bhpnet.py -t 129.168.0.1 -p 5555 -l -c"
    print "Bhpnet.py -t 129.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "Bhpnet.py -t 129.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "echo 'LOVEYA' | ./Bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)
    
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
        usage()
    
    #Read command line arguments
    
    try:
        opts,args = getopt(sys.argv[1:],"hle:t:p:cu",["help","listen","execute","target","port","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    
            
if __name__ == '__main__':
    main()