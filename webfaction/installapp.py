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
	api['server'].create_app(api['session_id'], 'webfactionapi', 'static', False, '')
	text = '<h1>Welcome from the Webfaction API!!1eleven</h1>'
	api['server'].write_file(api['session_id'], 'index.html', text)
	api['server'].create_website(api['session_id'],
		'webfactionapi_web',
		'75.125.135.130',
		False,
		['djingodjango.com', 'www.djingodjango.com'],
		['webfactionapi', '/'])

if __name__ == '__main__':
	main()

