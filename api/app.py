from config import IS_DEVELOPMENT
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
CORS(app)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=IS_DEVELOPMENT),
)
