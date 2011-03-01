from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sxsw.models import Party
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def byday(reqeuest, day):
	parties = Party.objects.filter(starttime__day=day)
	return render_to_response('sxsw/date_list.html', {'parties': parties, 'day': day, })

def byuser(request, user):
	u = User.objects.get(pk=user)
	parties = Party.objects.filter(attendees=u)
	return render_to_response('sxsw/user_list.html', {'parties': parties, 'user': u, })