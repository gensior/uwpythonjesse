#!/usr/bin/env python
# encoding: utf-8
"""
assignment1server.py

Created by Jesse Franceschini on 2011-01-15.
"""

import sys
import socket


def main():
	host = ''
	port = 50000
	backlog = 5
	size = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(backlog)
	while True:
		client, address = s.accept()
		data = client.recv(size)
		if data:
			addition = data.partition(',')
			client.send(str(int(addition[0]) + int(addition[2])))
			client.close()


if __name__ == '__main__':
	main()

