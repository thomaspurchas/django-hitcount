from django.conf.urls import patterns, url
from hitcount.views import update_hit_count_ajax

urlpatterns = patterns('',
    url('^hit/$',
        update_hit_count_ajax,
        name='hitcount_update_ajax'
    ),
)