from dataclasses import dataclass
from enum import StrEnum


class MessageType(StrEnum):
    UPDATE = "update"
    DELETE = "delete"


@dataclass
class TextMessage:
    id: str
    user_id: str
    type: MessageType
    text: str | None = None
    score: float | None = None







