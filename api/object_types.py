from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Project


class ProjectType(SQLAlchemyObjectType):
    class Meta:
        model = Project
