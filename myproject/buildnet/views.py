from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from buildnet.models import Part, Station, Installation
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect

def index(reqeuest):
	alpha = Installation.objects.filter(station=1)
	beta = Installation.objects.filter(station=2)
	parts = Part.objects.all().order_by('word')
	return render_to_response('buildnet/part_list.html', {'alpha': alpha, 'beta': beta, 'parts': parts })

def addpart(request, part, station):
	part = get_object_or_404(Part, pk=part)
	station = get_object_or_404(Station, name=station)
	installation = Installation(part=part, station=station)
	installation.save()
	return redirect('parts_list')