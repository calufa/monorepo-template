import pytest
from lib.db import reset_db, session
from models import Project


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

    assert result == {"data": {"projects": [{"name": "project-1"}]}}
