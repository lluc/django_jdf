from django.conf.urls import patterns, url

urlpatterns = patterns(
    'jdf_api.views',
    url(r'^places/(?P<pk>[0-9]+)$', 'place_detail', name='place_detail'),
    url(r'^places/name/(?P<place_name>.+)/$', 'place_name', name='place_name'),
    url(r'^places/search/(?P<place_name>.+)/$', 'search_place_name', name='place_name'),
)
