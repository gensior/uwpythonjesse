#!/usr/bin/env python
# encoding: utf-8
"""
webfaction.py

Created by Jesse Franceschini on 2011-01-31.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def login():
	from settings import WEBFACTION_USERNAME, WEBFACTION_PASSWORD
	import xmlrpclib
	server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
	session_id, account = server.login(WEBFACTION_USERNAME, WEBFACTION_PASSWORD)
	return {'server': server, 'session_id': session_id, 'account': account}

