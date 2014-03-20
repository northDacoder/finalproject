from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
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

    url(r'^api/', include(v1_api.urls)),

    url(r'^$', 'developer_app.views.angular', name="angular"),


    url(r'^register/developer/$', RegistrationView.as_view(success_url='/developer/new/'), name='registration_register_developer',),
    url(r'^register/company/$', RegistrationView.as_view(success_url='/company/new/'), name='registration_register_company',),
    url(r'^register/user/$', RegistrationView.as_view(success_url='/user/home/'), name='registration_register_developer',),

    #url(r'^accounts/login/', 'users.views.login_page', name='login'),
    url(r'^accounts/password/change/$', auth_views.password_change, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, name='password_change_done'),

    url(r'^accounts/password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),

    #and now add the registration urls
    url(r'accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)