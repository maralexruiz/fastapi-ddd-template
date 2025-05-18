from abc import ABC, abstractmethod
from typing import Optional

from template.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULAR


class NAME_CAPITALIZED_SINGULARRepository(ABC):
    """NAME_CAPITALIZED_SINGULARRepository defines a repository interface for NAME_CAPITALIZED_SINGULAR entity."""

    @abstractmethod
    def create(self, NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR) -> Optional[NAME_CAPITALIZED_SINGULAR]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[NAME_CAPITALIZED_SINGULAR]:
        raise NotImplementedError

    @abstractmethod
    def update(self, NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR) -> Optional[NAME_CAPITALIZED_SINGULAR]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
