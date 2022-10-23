from typing import List, Any
import starlette.websockets
from .search_schemas import SearchFilters, Filter
from api import Api
from fastapi import WebSocket
from elasticsearch_dsl import Search
from pydantic import BaseModel
from database.elastic import es


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


class SearchResponse(BaseModel):
    filters: list[Filter] = []
    response: list[str] = []


def db_query(query: str) -> SearchResponse:
    s = Search(using=es, index="product") \
        .query("query_string", query=query, default_field="name")
    response = s.execute()
    responses = [hit.name for hit in response]
    return SearchResponse(
        response=responses
    )


@api.get('/', response_model=SearchResponse)
async def search(query: str):
    obj = db_query(query)
    return obj
