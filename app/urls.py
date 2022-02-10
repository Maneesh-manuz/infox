from django.urls import re_path
from .import views


urlpatterns = [
    # re_path(r'^DEVindex$', views.DEVindex, name='DEVindex'),
    # re_path(r'^DEVprojects$', views.DEVprojects, name='DEVprojects'),
    # re_path(r'^DEVsuccess$', views.DEVsuccess, name='DEVsuccess'),
    # re_path(r'^DEVtable$', views.DEVtable, name='DEVtable'),
    # re_path(r'^DEVtask$', views.DEVtask, name='DEVtask'),
    # re_path(r'^DEVtaskform$', views.DEVtaskform, name='DEVtaskform'),
    # re_path(r'^DEVtaskmain$', views.DEVtaskmain, name='DEVtaskmain'),
    re_path(r'^manager_index$', views.manager_index, name='manager_index'),
    re_path(r'^manager_upprojects$', views.manager_upprojects, name='manager_upprojects'),
    re_path(r'^manager_newproject$', views.manager_newproject, name='manager_newproject'),
    re_path(r'^manager_description$', views.manager_description, name='manager_description'), 
    re_path(r'^manager_table$', views.manager_table, name='manager_table'), 
] 
