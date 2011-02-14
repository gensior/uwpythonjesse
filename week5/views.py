# Create your views here.
import json, time
from django.http import HttpResponse
import bookdb

def answer(request):
	req = {}
	req['time'] = time.time()
	req['uwnetid'] = 'gensior'
	try:
		a = request.GET['a']
	except KeyError:
		a = 0
	try:
		b = request.GET['b']
	except KeyError:
		b = 0
	req['result'] = int(a) + int(b)
	response = json.dumps(req)
	return HttpResponse(response, mimetype="application/json")

def listbooks(request):
	books = bookdb.BookDB()
	titles = books.titles()
	response = '<html><body>'
	for title in titles:
		response += "<a href='http://djingodjango.com/books/" + title['id'] + "'>" + title['title'] + "</a><br />"
	response += '</body></html>'
	return HttpResponse(response)

def details(self, id):
	books = bookdb.BookDB()
	titles = books.titles()
	info = books.title_info(id)
	response = '<html><head><title>' + info['title'] + '</title></head><body><a href="http://djingodjango.com/books">Books</a><br />'
	response += '<strong>Title</strong<br />' + info['title'] + '<br />'
	response += '<strong>Publisher</strong><br />' + info['publisher'] + '<br />'
	response += '<strong>ISBN</strong><br />' + info['isbn'] + '<br />'
	response += '<strong>Author</strong><br />' + info['author'] + '<br />'
	response += '</body></html>'
	return HttpResponse(response)
