from django.conf.urls import url
# from . import views
from crud.views import *
urlpatterns= [
    url(r'^$', MemberListView.as_view(), name='index'),
    url(r'^create$', MemberCreateView.as_view(), name='create'),
    # url(r'^edit/(?P<id>\d+)$', MemberUpdateView.as_view(), name='edit'),
    url(r'^update/(?P<pk>\d+)$', MemberUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$', MemberDeleteView.as_view(), name='delete'),
]