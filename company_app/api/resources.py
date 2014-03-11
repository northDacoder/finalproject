from django.conf import settings
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.fields import CharField
from tastypie.resources import ModelResource, Resource
from company_app.api.authorization import UserObjectsOnlyAuthorization
from company_app.models import CompanyProject, Company


class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = "company"
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class CompanyProjectResource(ModelResource):
    class Meta:
        queryset = CompanyProject.objects.all()
        resource_name = "companyproject"
        authorization = Authorization()



######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)