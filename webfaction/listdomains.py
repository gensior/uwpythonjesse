#!/usr/bin/env python
# encoding: utf-8
"""
listapps.py

Created by Jesse Franceschini on 2011-01-31.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import pprint
import webfaction

def main():
	api = webfaction.login()
	apps = api['server'].list_domains(api['session_id'])
	list_domains = []
	for app in apps:
		list_domains.append(app['domain'])
	list_domains.sort()
	for app in list_domains:
		print app


if __name__ == '__main__':
	main()

