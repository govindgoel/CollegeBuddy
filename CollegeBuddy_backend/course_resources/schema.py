import graphene
from course_resources.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required


class Resource_TypeObj(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return self['name']

class CoursesObj(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return self['name']


class ResourceObj(graphene.ObjectType):
    name = graphene.String()
    course = graphene.List(CoursesObj)
    details = graphene.String()
    resource_type = graphene.List(Resource_TypeObj)
    pdf = graphene.String()
    url = graphene.String()

    def resolve_name(self, info):
        return self['name']

    def resolve_details(self, info):
        return self['details']

    @login_required
    def resolve_pdf(self,info):
        return self['pdf']

    @login_required
    def resolve_url(self, info):
        return self['url']

    @graphene.resolve_only_args
    def resolve_resource_type(self):
        return Resource.objects.values().annotate(
            name=F('resource_type__name'),
        ).filter(id=self['id'])

    @login_required
    @graphene.resolve_only_args
    def resolve_course(self):
        return Resource.objects.values().annotate(
            name=F('course__name'),
        ).filter(id=self['id'])


class Query(graphene.ObjectType):
    resource = graphene.Field(ResourceObj,name=graphene.String(),resource_type=graphene.String())
    courses = graphene.List(CoursesObj)

    def resolve_resource(self, info, **kwargs):
        course = kwargs.get('course')
        resource_type = kwargs.get('resource_type')
        if course is not None:
            return Resource.objects.values().get(course=course)
        if resource_type is not None:
            return Resource.objects.values().get(resource_type=resource_type)
        else:
            raise APIException('Course is required',
                               code='COURSE_IS_REQUIRED')

    def resolve_courses(self, info):
        return Courses.objects.values().all()

schema = graphene.Schema(query=Query)
