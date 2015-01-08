from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter_clone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^tweet/', include('tweet.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
