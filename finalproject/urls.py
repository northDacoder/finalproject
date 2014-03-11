from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from company_app.api.resources import CompanyProjectResource, CompanyResource
from developer_app.api.resources import DeveloperResource, DeveloperProjectResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(DeveloperResource())
v1_api.register(DeveloperProjectResource())
v1_api.register(CompanyResource())
v1_api.register(CompanyProjectResource())

urlpatterns = patterns('',

    url(r'^$', 'developer_app.views.angular', name="angular"),

    url(r'^api/', include(v1_api.urls)),

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

    url(r'api/developers/doc/',
        include('tastypie_swagger.urls', namespace='tastypie_swagger'),
        kwargs={"tastypie_api_module": "v1_api",
                "namespace": "developer_tastypie_swagger"}
    ),
    url(r'api/companies/doc/',
        include('tastypie_swagger.urls', namespace='tastypie_swagger'),
        kwargs={"tastypie_api_module": "v1_api",
                "namespace": "company_tastypie_swagger"}
    )
)
