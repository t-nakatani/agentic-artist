from abc import ABC
from typing import Optional, Type

from pydantic import BaseModel


class Personality(BaseModel):
    name: str


class AgentPersona(ABC):
    role: str
    result_type: Type
    deps: Optional[Type] = None
