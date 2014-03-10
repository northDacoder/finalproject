from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'developer_app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^developers/$', 'developer_app.views.developers', name='developers'),
    url(r'^developers/new/$', 'developer_app.views.new_developer', name='new_developer'),
    url(r'^developers/(?P<developer_id>\w+)/$', 'developer_app.views.view_developer', name='view_developer'),
    url(r'^developers/(?P<developer_id>\w+)/edit/$', 'developer_app.views.edit_developer', name='edit_developer'),
    url(r'^developers/(?P<developer_id>\w+)/delete/$', 'developer_app.views.delete_developer', name='delete_developer'),

    url(r'^company/$', 'company_app.views.companies', name='companies'),
    url(r'^company/new/$', 'company_app.views.new_company', name='new_company'),
    url(r'^company/(?P<developer_id>\w+)/$', 'company_app.views.view_company', name='view_company'),
    url(r'^company/(?P<developer_id>\w+)/edit/$', 'company_app.views.edit_company', name='edit_company'),
    url(r'^company/(?P<developer_id>\w+)/delete/$', 'company_app.views.delete_company', name='delete_company'),

)
