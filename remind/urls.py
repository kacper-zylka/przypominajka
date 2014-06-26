from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rmnd import views


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', views.index),
    url(r'^$', views.EventList.as_view(), name='event_list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/$', views.EventList.as_view(), name='event_list'),
    url(r'^events/(?P<event_id>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
    url(r'^new_event/$', views.new_event, name='new_event'),
)
