import graphene
from lib.db import session
from models import Project
from object_types import ProjectType


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)

    def resolve_projects(parent, info):
        return session.query(Project).all()


schema = graphene.Schema(query=Query)
