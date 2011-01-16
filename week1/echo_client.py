#!/usr/bin/env python
# encoding: utf-8
"""
echo_client.py

Created by Jesse Franceschini on 2011-01-15.
"""

import socket

def main():
	host = 'localhost'
	port = 50000
	size = 1024
	s = socket.socket(socket.AF_INET,
					  socket.SOCK_STREAM)
	s.connect((host,port))
	s.send('Hello, world!')
	data = s.recv(size)
	s.close
	print 'Received:', data


if __name__ == '__main__':
	main()

