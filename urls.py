from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#Allows you to include(appname.urls) instead of include(apps.appname.urls)
import conf.paths


urlpatterns = patterns('',
	#Change these as needed
	#This app will live at the root of site
    url(r'^', include('sampleapp.urls')),
    #grappelli for sweet looking admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)