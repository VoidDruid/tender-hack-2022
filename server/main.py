from functools import partial
from typing import Dict

from api import make_app
from base_schemas import OkResponse
from loguru import logger
from routes import search_api
from starlette.middleware.cors import CORSMiddleware

from common.logger import init_logger
from settings import DEBUG, LOG_FORMAT, LOG_LEVEL, server_settings

logger.info(f"Running with config: {server_settings.dict()}")

app = make_app()

include_router = partial(app.include_router, prefix='/api')

if not DEBUG:
    # Init logger in JSON format
    init_logger(
        LOG_LEVEL,
        LOG_FORMAT,
        keep_loggers=["uvicorn.access"],
        suppress_loggers=["uvicorn", "uvicorn.error", "fastapi"],
    )
else:
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/healthz", tags=["health check"], response_model=OkResponse)
async def root() -> Dict[str, bool]:
    """Health check endpoint"""
    return {"ok": True}


include_router(search_api)
