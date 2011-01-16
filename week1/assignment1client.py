#!/usr/bin/env python
# encoding: utf-8
"""
assignment1client.py

Created by Jesse Franceschini on 2011-01-15.
"""

import sys
import socket


def main():
	host = 'block115405-xg5.blueboxgrid.com'
	port = 50000
	size = 1024
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(str(sys.argv[1])+','+str(sys.argv[2]))
	data = s.recv(size)
	s.close
	print 'Sum:', data


if __name__ == '__main__':
	main()

