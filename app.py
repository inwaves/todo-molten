from molten import App, Route, ResponseRendererMiddleware
from wsgicors import CORS

from auth import AuthorizationMiddleware
from database import DBComponent
from models import TodoManagerComponent
from routes import create_todo, get_docs, get_schema

app = App(
    components=[
        DBComponent(),
        TodoManagerComponent(),
    ],
    middleware=[
        ResponseRendererMiddleware(),
        AuthorizationMiddleware,
    ],
    routes=[
        Route("/_docs", get_docs),
        Route("/_schema", get_schema),
        Route("/todos", create_todo, method="POST"),
    ],
)

app = CORS(app, headers="*", methods="*", origin="*", maxage="86400")
