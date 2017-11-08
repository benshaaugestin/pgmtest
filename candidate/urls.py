from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^submit/$', login_required(views.rand), name='submit'),
    url(r'^compile/(?P<num>[-\d]+)/',login_required( views.CompileView.as_view()), name="compile"),
    url(r'^coding/(?P<pk>[-\d]+)/', login_required(views.DetailsView.as_view()), name='detail'),
    url(r'^queslist', login_required(views.IndexView.as_view()), name='index'),

    ]