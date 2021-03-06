from django.conf.urls.defaults import *
from sxsw.models import Party

info_dict = {
	'queryset': Party.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
	(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='sxsw/party_detail.html'), ),
	(r'^mar(?P<day>\d{2})/$', 'sxsw.views.byday'),
	(r'^user/(?P<user>\d+)/$', 'sxsw.views.byuser'),
)    