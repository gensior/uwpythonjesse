from django.conf.urls.defaults import *
from buildnet.models import Station, Part, Installation

info_dict = {
	# 'queryset': Part.objects.all(),
}

urlpatterns = patterns('',
	url(r'^$', 'buildnet.views.index', name="parts_list"),
	(r'^(?P<part>\d+)/(?P<station>\w+)/add$', 'buildnet.views.addpart'),
	(r'^(?P<part>\d+)/remove$', 'buildnet.views.removepart'),
	(r'^(?P<part>\d+)/install$', 'buildnet.views.install'),
	# (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='sxsw/party_detail.html'), ),
	# (r'^mar(?P<day>\d{2})/$', 'sxsw.views.byday'),
	# (r'^user/(?P<user>\d+)/$', 'sxsw.views.byuser'),
)                 