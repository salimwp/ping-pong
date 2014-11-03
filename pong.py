"""
Copyright (c) 2014 Salim Haniff <salimwp@gmail.com>

This file is part of ping-pong.

Neo4j is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""


import socket
import errno
from socket import error as socket_error
import time
import sys

def createFileName():
	time.strftime("%Y%m%d%H%m%S")

TCP_IP = socket.gethostbyname(socket.getfqdn());
BUFFER_SIZE=1024
TCP_PORT_RANGE = range(1,65535)


for port in TCP_PORT_RANGE:
	try:
		sys.stdout.write("\r                                            ")
		sys.stdout.write("\rAttempt to bind to port: %d" % port)
		sys.stdout.flush()
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		sock.bind((TCP_IP, port))
		sock.listen(1)
		conn, addr = sock.accept()
		data = conn.recv(BUFFER_SIZE)
		if not data: break;
		#print "received data:" , data
		conn.send("PONG!")
		conn.close()
		sock.close()
	except socket_error as serr:
		sys.stdout.write(" : %s" % errno.errorcode[serr.errno])
	
