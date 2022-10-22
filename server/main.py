from functools import partial
from typing import Dict

from loguru import logger

from api import make_app
from base_schemas import OkResponse
from common.logger import init_logger
from settings import server_settings, DEBUG, LOG_LEVEL, LOG_FORMAT

from routes import search_api

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


@app.get("/healthz", tags=["health check"], response_model=OkResponse)
async def root() -> Dict[str, bool]:
    """Health check endpoint"""
    return {"ok": True}


include_router(search_api)

