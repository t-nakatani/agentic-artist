from abc import ABC
from typing import Type

from pydantic import BaseModel


class Personality(BaseModel):
    name: str


class AgentPersona(ABC):
    role: str
    result_type: Type
