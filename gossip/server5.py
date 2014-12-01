'''
	Role : Terminating node of the binary tree with implements gossip algorithm
		once the message reaches this node, it is not passed to any other
'''

import socket
import time

soc = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = "127.0.0.1"
port = 7006
soc.bind((host, port)) 
print "Server 5 started on port {0}...".format(port)

counter = 0
incoming_data = list(range(20))
while counter>-1:
	packet, addr = soc.recvfrom(1024)		
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"	
	print 'Source	: {0} | time	: {1}\n'.format(addr[1], time.ctime(time.time()))
	print "Message 	: {0}".format(packet)
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	counter+=1
	
soc.close() # Close the connection

