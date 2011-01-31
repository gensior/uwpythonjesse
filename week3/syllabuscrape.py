#!/usr/bin/env python
# encoding: utf-8
"""
syllabuscrape.py

Created by Jesse Franceschini on 2011-01-30.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib
import urllib2
import shutil
from BeautifulSoup import BeautifulSoup

syllabusurl = "http://briandorsey.info/uwpython/Internet_Programming_in_Python.html"
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13'
opener = urllib2.build_opener()

def main():
	shutil.rmtree('./syllabus', ignore_errors = True)
	os.mkdir('./syllabus')
	request = urllib2.Request(syllabusurl)
	request.add_header('User-Agent', user_agent)
	html = opener.open(request).read()
	soup = BeautifulSoup(html)
	rows = soup.find('table').findAllNext('tr')
	for row in rows:
		try:
			week = row.findNext('td').findNext('td').findNext('td')['id']
			os.mkdir('./syllabus/' + week)
		except KeyError:
			continue
		mkdirectory(row.findNext('td').findNext('td').findNext('td').findAll('a'), directory = 'topic', week = week)
		mkdirectory(row.findNext('td').findNext('td').findNext('td').findNext('td').findAll('a'), directory = 'readings', week = week)

def mkdirectory(data, directory, week):
	os.mkdir('./syllabus/' + week + '/' + directory)
	gatherlinks(data, directory = directory, week = week)
			
def urlify(text):
	if text.startswith('http'):
		return text
	else:
		return "http://briandorsey.info/uwpython/" + text

def filetype(text):
	if text.endswith('.pdf'):
		return '.pdf'
	else:
		return '.html'

def gatherlinks(links, directory, week):
	for link in links:
		f = open('./syllabus/' + week + '/' + directory + '/' + link.text.replace(' ', '_').replace('/','_') + filetype(link['href']), 'w')
		request = urllib2.Request(urlify(link['href']))
		request.add_header('User-Agent', user_agent)
		f.write(opener.open(request).read())
		f.close()

if __name__ == '__main__':
	main()

