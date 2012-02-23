from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	#App specific urls
    url(r'^$', 'sampleapp.views.home', name='home'),
)
