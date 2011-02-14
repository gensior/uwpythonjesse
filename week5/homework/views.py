# Create your views here.
import json, time
from django.http import HttpResponse

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