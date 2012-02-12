from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	#App specific urls
    url(r'^$', 'apps.sample_one.views.home', name='home'),
)
