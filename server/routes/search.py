from api import Api
from fastapi import WebSocket
from fastapi.responses import HTMLResponse

api: Api = Api(

)

@api.websocket("/ws")
async def websocked_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_text(f"Received object: {data}")