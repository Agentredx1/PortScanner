#Simplest port scanner
#Simon Greenaway
#Made following geeksforgeeks socket tutorial
import sys
import socket

#Can take 2 arguements when ran from command line
#first is IP address or Domain Name
#second is specified port we want to check
if len(sys.argv) ==3:
    hostIP = socket.gethostbyname(sys.argv[1])
    targetPort = int(sys.argv[2])
else:
    hostIP = socket.gethostbyname("scanme.nmap.org")
    targetPort = 22
    #if no arguements given, default to this scanme page and a port known to be open
    #80 is also open.

print("Scanning: {}".format(hostIP))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    response = s.connect_ex((hostIP,targetPort))
    if response ==0:
        print("Port {} is open".format(targetPort))
    s.close

except:
    print("Something went wrong")

print("Done scanning")