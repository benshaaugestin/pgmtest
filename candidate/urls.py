from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^submit/$', views.rand, name='submit'),
    url(r'^compile/(?P<num>[-\d]+)/', views.CompileView.as_view(), name="compile"),
    url(r'^coding/', views.DetailView.as_view(), name='detail'),
    url(r'^queslist', views.IndexView.as_view(), name='index'),

    ]