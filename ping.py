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

def usage():
	print "python ping.py <ip_address>"
	sys.exit(0)

class Results:
	networkResult = [];

	def __init__(self):
		print ""

	def add(self, port, result):
		self.networkResult.append([port,result]);

	def printReport(self):
		for result in self.networkResult:
			print result


#print str(sys.argv[1])
#sys.exit(0)

try:
	#TCP_IP = socket.gethostbyname(socket.getfqdn());
	socket.inet_aton(sys.argv[1])
	TCP_IP = sys.argv[1]
except socket.error:
	print "Supplied IP address not valid"
	usage()


BUFFER_SIZE=1024
TCP_PORT_RANGE = range(1,65535)

result = Results()

for port in TCP_PORT_RANGE:
	try:
		#print "Attempt to bind to port: ", port
		sys.stdout.write("\rTest progress %d/65535" % port)
		sys.stdout.flush()
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		sock.settimeout(5)
		sock.connect((TCP_IP, port))
		sock.send("PING!")
		data = sock.recv(BUFFER_SIZE)
		#print data
		sock.close()
		result.add(port, data)
		time.sleep(0.05)
	except socket_error as serr:
		try:
			#print errno.errorcode[serr.errno]
			result.add(port,errno.errorcode[serr.errno])
		except KeyError:
			#print "error code not found"
			result.add(port,"unknown")
	

result.printReport()
