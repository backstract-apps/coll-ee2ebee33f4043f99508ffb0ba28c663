from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Items(BaseModel):
    id: Any
    name: str
    description: str
    quantity: int


class ReadItems(BaseModel):
    id: Any
    name: str
    description: str
    quantity: int
    class Config:
        from_attributes = True




class PostItems(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    quantity: int = Field(...)

    class Config:
        from_attributes = True



class PutItemsId(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    quantity: int = Field(...)

    class Config:
        from_attributes = True



class DeleteItemsId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True

