import json
from typing import List

from api import Api
from fastapi import WebSocket
from fastapi.responses import HTMLResponse

api: Api = Api(

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
