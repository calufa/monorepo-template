import pytest
from graphene.test import Client
from lib.db import reset_db, session
from models import Project
from schema import schema


@pytest.fixture(autouse=True)
def before():
    reset_db()


def test():
    """
    Test GraphQL API end-to-end
    """
    project = Project(name="project-1")
    session.add(project)
    session.commit()

    result = Client(schema).execute(
        """
        {
            projects {
                name
            }
        }
        """
    )
    assert result == {"data": {"projects": [{"name": "project-1"}]}}
