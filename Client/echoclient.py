#!/usr/bin/env python

"""
Author: Timothy Jones
Project: Echo Server/Client
Language: Python
Date: 10/6/2013
Reference: http://ilab.cs.byu.edu/python/socket/echoserver.html
Notes:
"""

import sys, socket # import sys for commandline arguments and socket for networking packages

if ( len(sys.argv) >= 4 ) :
	message = sys.argv[3] # gets user message
else:
	message = "this is a test message" # default test message
	
if ( len(sys.argv) >= 3 ) :
	port = int(sys.argv[2]) # gets user port
else:
	port = 50000 # default port is 50000
	
if ( len(sys.argv) >= 2 ) :
	host = sys.argv[1] # gets user host, this can be an ip address
else:
	host = 'localhost' # default host is the localhost (127.0.0.1)

size = 1024 # chunk size for receiving

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sets up socket
	s.connect((host,port)) # connects to server
except socket.error as e: # catches socket exceptions and outputs error
	if s:
		s.close() # close socket
	print ("Could not open socket: ", message)
	sys.exit(1) # close program
print ("Client has connected to the server!") # tells user we've connected to the server
s.send(bytes(message, 'UTF-8')) # decodes message to bytes (utf-8) and sends
print ("Client sent message: ", message)
data = s.recv(size) # receives response from server
s.close() # closes socket
print ("Received: ", str(data, 'UTF-8')) # encodes bytes to utf-8 and outputs result
sys.exit(1)
