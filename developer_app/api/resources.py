from django.conf import settings
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.fields import CharField
from tastypie.resources import ModelResource, Resource
from developer_app.api.authorization import UserObjectsOnlyAuthorization
from developer_app.models import Project, Developer


class DeveloperResource(ModelResource):
    class Meta:
        queryset = Developer.objects.all()
        resource_name = "developer"
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class DeveloperProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = "developerproject"
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