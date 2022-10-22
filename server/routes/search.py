import json
from typing import List, Any

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
    while True:
        query: str = await websocket.receive_text()
        response_obj = get_autocomplete_options(query)
        await websocket.send_json(json.dumps(response_obj))


def db_query(query: str) -> dict: ...


@api.get('/')
async def search(query: str):
    obj = db_query(query)
    return obj
