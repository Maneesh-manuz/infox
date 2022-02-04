from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.DEVindex, name='DEVindex'),
    re_path(r'^DEVprojects$', views.DEVprojects, name='DEVprojects'),
    re_path(r'^DEVsuccess$', views.DEVsuccess, name='DEVsuccess'),
    re_path(r'^DEVtable$', views.DEVtable, name='DEVtable'),
    re_path(r'^DEVtask$', views.DEVtask, name='DEVtask'),
    re_path(r'^DEVtaskform$', views.DEVtaskform, name='DEVtaskform'),
    re_path(r'^DEVtaskmain$', views.DEVtaskmain, name='DEVtaskmain'),
]