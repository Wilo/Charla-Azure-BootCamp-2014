#!/usr/bin/env python
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('djangositeabc.apps.tableservice.views',
                          url(r'^list_tasks$', 'list_tasks'),
	                      url(r'^add_task$', 'add_task'),
	                      url(r'^update_task$', 'update_task'),
)