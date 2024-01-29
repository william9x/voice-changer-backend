import logging

import uvicorn
from fastapi import FastAPI, HTTPException

import docs
import events
from api.router import api as api_router
from api.router import api_v1 as api_v1_router

logger = logging.getLogger(__name__)

app = FastAPI(title=docs.title, description=docs.desc)

# include router
app.include_router(api_router)
app.include_router(api_v1_router)

# add middleware
# add exception handler
app.add_exception_handler(HTTPException, events.on_http_error)


def main():
    config = uvicorn.Config(
        "main:app",
        host="0.0.0.0",
        port=8080,
        log_level="debug",
        workers=10,
    )
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
