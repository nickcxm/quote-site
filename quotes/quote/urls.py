from django.conf.urls import url
from . import views
app_name='quote'

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^add/$',views.add,name='add'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^search/$',views.search,name='search')
]