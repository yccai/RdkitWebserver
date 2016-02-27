from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rdkit_webserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^smiles/', include('smiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
