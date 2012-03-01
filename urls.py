from django.conf.urls.defaults import patterns, include, url

#Uncomment the next two lines to enable the built in django admin
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
    #Uncomment the next line to enable the built in django admin also uncomment settings for admin
    url(r'^admin/', include(admin.site.urls)),
)