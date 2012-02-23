from django.conf.urls.defaults import patterns, include, url

#Uncomment the next two lines to enable the built in django admin
#from django.contrib import admin
#admin.autodiscover()


urlpatterns = patterns('',
	#Change these as needed
	#This app will live at the root of site
    url(r'^', include('apps.sampleapp.urls')),
    #Uncomment the next line to enable the built in django admin
    #url(r'^admin/', include(admin.site.urls)),
)