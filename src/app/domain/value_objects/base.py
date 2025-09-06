from dataclasses import dataclass
from typing import Any

from app.domain.exceptions.base import DomainFieldError


@dataclass
class ValueObject:
    value: Any

    def __post_init__(self):
        if self.value is None:
            raise DomainFieldError('ValueObject.value cant be none')