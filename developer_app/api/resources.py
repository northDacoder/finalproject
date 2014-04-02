from django.conf import settings
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.fields import CharField, ToManyField
from tastypie.resources import ModelResource, Resource
from developer_app.api.authorization import UserObjectsOnlyAuthorization
from developer_app.models import DeveloperProject, Developer


class BareDeveloperProjectResource(ModelResource):
    class Meta:
        queryset = DeveloperProject.objects.all()
        resource_name = "bare_projects"

class DeveloperProjectResource(ModelResource):
    class Meta:
        queryset = DeveloperProject.objects.all()
        resource_name = "developerproject"
        authorization = Authorization()

class DeveloperResource(ModelResource):
    projects = ToManyField(BareDeveloperProjectResource, 'developer_projects', full=True, null=True)

    class Meta:
        queryset = Developer.objects.all()
        resource_name = "developer"
        # authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()




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