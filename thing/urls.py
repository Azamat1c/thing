from django.conf.urls import patterns, include, url
#from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'thing.views.log_in'),
    url(r'^logout', 'thing.views.log_out'),
)
