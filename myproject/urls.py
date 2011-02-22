from django.conf.urls.defaults import *
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
	(r'^polls/', include('polls.urls')),
    (r'^week4/', include('homework.urls')),
    (r'^books/$', views.listbooks),
    (r'^books/(?P<id>id\d)$', views.details),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
