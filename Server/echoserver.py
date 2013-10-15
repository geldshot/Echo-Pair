"""
Author: Timothy Jones
Project: Echo Server/Client
Language: Python
Date: 10/6/2013
Reference: http://ilab.cs.byu.edu/python/socket/echoserver.html
http://docs.python.org/2/howto/sockets.html
Notes: host is important! if this server is setup as localhost then it becomes
only available to clients on the same machine. leaving host blank makes it available
through any address the server happens to have. specifying the host makes it reachable
through that address only. Also, this server isn't prepared to handle messages of
more than 1024 utf-8 bytes. 
"""

import sys, socket # import sys for commandline arguments and socket for networking packages
	
if ( len(sys.argv) >= 2 ) :
	port = int(sys.argv[1]) # assign to port provided by user
else:
	port = 50000 # default to port 5000 if no port provided

host = socket.gethostname() # gets the hostname required for outside interaction
backlog = 5 # going to use this to determine the max size of our queue
size = 1024 # message size

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sets up socket
	s.bind((host, port)) # binds socket and specifies port to listen to
	s.listen(backlog) # sets the maximum queue
except socket.error as e: # catches socket exception
	
	if s:
		s.close() # close socket
	print ("Could not open socket: ", e)
	sys.exit(1) # exit server
	
localaddress = socket.gethostbyname(socket.gethostname()) # get host address

print( "Server is at address: ", localaddress)
print( "Server is using port: ", port)

client, address = s.accept() # gets client object and address
data = client.recv(size) # get first chunk of up to 1024 bytes

print( "Server connected to client at address: ", address)

if data: # if there is a message
    print( "Server received message: ", str(data, 'UTF-8')) # outputs utf-8 encoded message
    client.send(data) # returns message
client.close() # closes socket
sys.exit(1)
