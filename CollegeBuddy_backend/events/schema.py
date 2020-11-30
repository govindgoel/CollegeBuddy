import graphene
from events.models import *
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required

class EventsObj(graphene.ObjectType):
    name = graphene.String()
    slug = graphene.String()
    details = graphene.String()
    creator = graphene.String()
    date = graphene.DateTime()
    event_type = graphene.String()
    location = graphene.String()

    def resolve_name(self, info):
        return self['name']

    def resolve_slug(self, info):
        return self['slug']

    def resolve_details(self, info):
        return self['details']

    @login_required
    def resolve_creator(self, info):
        return User.objects.values().get(id=self['creator_id'])

    @login_required
    def resolve_date(self, info):
        return self['date']

    def resolve_event_type(self, info):
        return self['event_type']

    @login_required
    def resolve_location(self,info):
        return self['location']

class Query(graphene.ObjectType):
    events = graphene.List(EventsObj)
    event = graphene.Field(EventsObj, slug=graphene.String(required=True))

    @login_required
    def resolve_events(self, info):
        return Event.objects.values().all()

    def resolve_event(self, info, **kwargs):
        slug = kwargs.get('slug')
        if slug is not None:
            return Event.objects.values().get(slug=slug)
        else:
            raise APIException('Slug is required',
                               code='SLUG_IS_REQUIRED')


schema = graphene.Schema(query=Query)
