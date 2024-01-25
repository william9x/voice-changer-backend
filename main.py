import logging

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

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
logger.info('Adding middlewares..')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
app.add_exception_handler(HTTPException, events.on_http_error)
