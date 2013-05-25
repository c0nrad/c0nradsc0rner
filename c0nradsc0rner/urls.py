from django.conf.urls import patterns, include, url
from blog.models import Blog
from django.conf import settings
from blog import views

# AJAX
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
    
urlpatterns = patterns('',
                       
    url(r'^$', 'blog.views.index'),
    url(r'^page/(\d+)', 'blog.views.index', name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', views.view_category,  name='view_blog_category'),
    url(r'^aboutme.html$', views.aboutme, name="view_blog_aboutme"),
    url(r'^contactMe.html$', views.contactMe, name="view_blog_contactMe"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('bitcoin.views',
    url(r'^bitcoin/$', 'allOrNothing'),
)

urlpatterns += patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),                    
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
