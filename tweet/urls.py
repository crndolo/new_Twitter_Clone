from django.conf.urls import patterns, include, url
from tweet import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.tweets, name='tweets'),
    # url(r'^blog/', include('blog.urls')),
)
