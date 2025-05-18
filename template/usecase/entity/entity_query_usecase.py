from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULARNotFoundError

from .NAME_LOWER_SINGULAR_query_model import NAME_CAPITALIZED_SINGULARReadModel
from .NAME_LOWER_SINGULAR_query_service import NAME_CAPITALIZED_SINGULARQueryService


class NAME_CAPITALIZED_SINGULARQueryUseCase(ABC):
    """NAME_CAPITALIZED_SINGULARQueryUseCase defines a query usecase inteface related NAME_CAPITALIZED_SINGULAR
    entity."""

    @abstractmethod
    def fetch_NAME_LOWER_SINGULAR_by_id(self, id: int) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_NAME_LOWER_PLURAL(self) -> List[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError


class NAME_CAPITALIZED_SINGULARQueryUseCaseImpl(NAME_CAPITALIZED_SINGULARQueryUseCase):
    """NAME_CAPITALIZED_SINGULARQueryUseCaseImpl implements a query usecases related NAME_CAPITALIZED_SINGULAR
    entity."""

    def __init__(self, NAME_LOWER_SINGULAR_query_service: NAME_CAPITALIZED_SINGULARQueryService):
        self.NAME_LOWER_SINGULAR_query_service: NAME_CAPITALIZED_SINGULARQueryService = NAME_LOWER_SINGULAR_query_service

    def fetch_NAME_LOWER_SINGULAR_by_id(self, id: int) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        try:
            NAME_LOWER_SINGULAR = self.NAME_LOWER_SINGULAR_query_service.find_by_id(id)
            if NAME_LOWER_SINGULAR is None:
                raise NAME_CAPITALIZED_SINGULARNotFoundError
        except Exception:
            raise

        return NAME_LOWER_SINGULAR

    def fetch_NAME_LOWER_PLURAL(self) -> List[NAME_CAPITALIZED_SINGULARReadModel]:
        try:
            NAME_LOWER_PLURAL = self.NAME_LOWER_SINGULAR_query_service.find_all()
        except Exception:
            raise

        return NAME_LOWER_PLURAL
