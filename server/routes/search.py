import json
from typing import List, Any

import starlette.websockets

from api import Api
from fastapi import WebSocket
from fastapi.responses import HTMLResponse

api: Api = Api(
    prefix='/search',
    tags=['Search API']
)


def get_autocomplete_options(query: str) -> List[str]:
    return ['Lol', 'Kek', 'Cheburek']


@api.websocket("/autocomplete")
async def autocomplete(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            query: str = await websocket.receive_text()
            response_obj = get_autocomplete_options(query)
            await websocket.send_json(response_obj)
    except starlette.websockets.WebSocketDisconnect:
        ...


def db_query(query: str) -> dict: ...


@api.get('/')
async def search(query: str):
    obj = db_query(query)
    return obj
