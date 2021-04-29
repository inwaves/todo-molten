from typing import Any, Callable, Optional

from molten import HTTP_403, HTTPError, Header, Request


def AuthorizationMiddleware(handler: Callable[..., Any]) -> Callable[..., Any]:
    def middleware(request: Request, authorization: Optional[Header]) -> Any:
        if authorization != "Bearer secret" and request.path not in ["/_docs", "/_schema"]:
            raise HTTPError(HTTP_403, {"error": "forbidden"})
        return handler()

    return middleware
