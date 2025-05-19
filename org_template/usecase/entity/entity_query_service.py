from abc import ABC, abstractmethod
from typing import List, Optional

from .NAME_LOWER_SINGULAR_query_model import NAME_CAPITALIZED_SINGULARReadModel


class NAME_CAPITALIZED_SINGULARQueryService(ABC):
    """NAME_CAPITALIZED_SINGULARQueryService defines a query service inteface related NAME_CAPITALIZED_SINGULAR
    entity."""

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError
