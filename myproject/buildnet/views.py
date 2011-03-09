from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from buildnet.models import Part, Station, Installation
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect

def index(reqeuest):
	alpha = Installation.objects.filter(station=1)
	beta = Installation.objects.filter(station=2)
	parts = Installation.objects.filter(station=3)
	return render_to_response('buildnet/part_list.html', {'alpha': alpha, 'beta': beta, 'parts': parts })

def addpart(request, part, station):
	station = get_object_or_404(Station, name=station)
	installation = get_object_or_404(Installation, pk=part)
	installation.station = station
	installation.save()
	return redirect('parts_list')

def removepart(request, part ):
	installation = get_object_or_404(Installation, pk=part)
	installation.station = get_object_or_404(Station, pk=3)
	installation.installed = False
	installation.save()
	return redirect('parts_list')

def install(request, part ):
	installation = get_object_or_404(Installation, pk=part)
	if installation.could_be_installed:
		installation.installed = True
		installation.save()
	else:
		error = 'Cannot be installed out of order.'
	return redirect('parts_list')