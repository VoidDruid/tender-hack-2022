from typing import Union

from pydantic import BaseModel


class Option(BaseModel):
    id: int
    value: str


class Range(BaseModel):
    from_: int
    to: int


class Filter(BaseModel):
    type: str
    name: str
    options: Union[list[Option], Range] = []


class SearchFilters(BaseModel):
    filters: list[Filter] = []
