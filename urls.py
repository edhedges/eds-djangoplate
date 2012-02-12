from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	#Change these as needed
	#This app will live at the root of site
    url(r'^', include('apps.sample_one.urls')),
    #This app will live at the root/sample-two
    url(r'^sample-two/', include('apps.sample_two.urls')),
    #This is the sweet custom django admin at root/admin
    url(r'^admin/', include(admin.site.urls)),
)