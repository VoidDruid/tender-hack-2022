from pydantic import BaseModel

from api import Api


api: Api = Api(
    prefix='/test',
    tags=['API for test'],
)


class Mem(BaseModel):
    text_mema: str


@api.post('/lol')
def method(mem: Mem):
    return {'lol': mem.text_mema}
