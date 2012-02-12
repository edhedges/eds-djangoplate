from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	#App specific urls
	url(r'^$', 'apps.sample_two.views.home', name='home'),
)
