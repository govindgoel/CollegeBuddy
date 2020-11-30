import graphene
from info.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required


class NoticeObj(graphene.ObjectType):
    title = graphene.String()
    details = graphene.String()
    pdf = graphene.String()
    url = graphene.String()
    pinned = graphene.Boolean()

    def resolve_title(self, info):
        return self['title']

    def resolve_details(self, info):
        return self['details']

    @login_required
    def resolve_pdf(self,info):
        return self['pdf']

    @login_required
    def resolve_url(self, info):
        return self['url']


class Query(graphene.ObjectType):
    notices = graphene.List(NoticeObj)

    def resolve_notices(self, info):
        return Notice.objects.values().all()

schema = graphene.Schema(query=Query)
