import socket  # Import socket module
import time
import random

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 7007
soc.bind((host, port))

print "Child Three(7007) started on port {0}...".format(port)

while True:
    packet, addr = soc.recvfrom(1024)
    time.sleep(2)
    print 'Source	: {0} | time	: {1}\n'.format(addr[1], time.ctime(time.time()))
    print "Message 	: {0}".format(packet)
    ports = [7006, 7003]

    port_selected = random.choice(ports)
    if not port_selected:
        print "This node has no child to send data to!!"
    else:
        soc.sendto(packet, (host, port_selected))  # address to send the message to contains [host : port]
        print "Message: {0} sent to {1}\n".format(packet, port_selected)
        time.sleep(1)

soc.close()  # Close the connection