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
	apps = api['server'].list_apps(api['session_id'])
	list_apps = []
	for app in apps:
		list_apps.append(app['name'])
	list_apps.sort()
	for app in list_apps:
		print app


if __name__ == '__main__':
	main()

