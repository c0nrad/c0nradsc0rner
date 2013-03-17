from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from blog.models import Blog

from blog import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', 'blog.views.index'),
    url(r'^index.html$', redirect_to, {'url': '/'}),
    url(r'^blog/view/(?P<slug>[^\.]+).html', 
        views.view_post, 
        name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', views.view_category,  name='view_blog_category'),
    url(r'^aboutme.html$', views.aboutme, name="view_blog_aboutme"),
        
                       # Examples:
    # url(r'^$', 'c0nradsc0rner.views.home', name='home'),
    # url(r'^c0nradsc0rner/', include('c0nradsc0rner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
