from abc import ABC, abstractmethod
from typing import Optional

from template.domain.book import NAME_CAPITALIZED_SINGULA


class Bookepository(ABC):
    """Bookepository defines a repository interface for NAME_CAPITALIZED_SINGULA entity."""

    @abstractmethod
    def create(self, book: NAME_CAPITALIZED_SINGULA) -> Optional[NAME_CAPITALIZED_SINGULA]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[NAME_CAPITALIZED_SINGULA]:
        raise NotImplementedError

    @abstractmethod
    def update(self, book: NAME_CAPITALIZED_SINGULA) -> Optional[NAME_CAPITALIZED_SINGULA]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
