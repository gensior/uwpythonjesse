#!/usr/bin/env python
# encoding: utf-8
"""
installapp.py

Created by Jesse Franceschini on 2011-01-31.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import webfaction

def main():
	api = webfaction.login()
	cmd = "cd ~/webapps/webfactionapi/"
	api['server'].system(api['session_id'], cmd)
	text = '<h1>This was edited from the API, you guys.</h1>'
	api['server'].write_file(api['session_id'], 'webapps/webfactionapi/index.html', text)

if __name__ == '__main__':
	main()

