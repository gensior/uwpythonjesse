# Create your views here.
import json, time, cgi
from django.http import HttpResponse

def answer(request):
	parsed = cgi.parse_qs(request.META['QUERY_STRING'])
	req = {}
	req['time'] = time.time()
	req['uwnetid'] = 'gensior'
	req['result'] = int(parsed['a'][0]) + int(parsed['b'][0])
	response = json.dumps(req)
	return HttpResponse(response, mimetype="application/json")