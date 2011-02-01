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
	api['server'].delete_app(api['session_id'], 'webfactionapi')
	api['server'].delete_website(api['session_id'],
		'webfactionapi_web',
		'75.125.135.130',
		False,)

if __name__ == '__main__':
	main()

