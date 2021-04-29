from molten.openapi import OpenAPIUIHandler, OpenAPIHandler, Metadata, HTTPSecurityScheme

from models import Todo, TodoManager

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="Todo-backend",
        description="todo-backend",
        version="0.0.0",
    ),
    security_schemes=[
        HTTPSecurityScheme("default", "bearer"),
    ],
    default_security_scheme="default"
)

get_docs = OpenAPIUIHandler()


def create_todo(todo: Todo, todo_manager: TodoManager) -> Todo:
    return todo_manager.create(todo)
