from abc import ABC, abstractmethod
from typing import Optional, cast

from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULAR, NAME_CAPITALIZED_SINGULARNotFoundError, NAME_CAPITALIZED_SINGULARRepository

from .NAME_LOWER_SINGULAR_command_model import NAME_CAPITALIZED_SINGULARCreateModel, NAME_CAPITALIZED_SINGULARUpdateModel
from .NAME_LOWER_SINGULAR_query_model import NAME_CAPITALIZED_SINGULARReadModel


class NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork(ABC):
    """NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork defines an interface based on Unit of
    Work pattern."""

    NAME_LOWER_SINGULAR_repository: NAME_CAPITALIZED_SINGULARRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class NAME_CAPITALIZED_SINGULARCommandUseCase(ABC):
    """NAME_CAPITALIZED_SINGULARCommandUseCase defines a command usecase inteface related NAME_CAPITALIZED_SINGULAR
    entity."""

    @abstractmethod
    def create_NAME_LOWER_SINGULAR(self, data: NAME_CAPITALIZED_SINGULARCreateModel) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_NAME_LOWER_SINGULAR(
        self, id: str, data: NAME_CAPITALIZED_SINGULARUpdateModel
    ) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_NAME_LOWER_SINGULAR_by_id(self, id: str):
        raise NotImplementedError


class NAME_CAPITALIZED_SINGULARCommandUseCaseImpl(NAME_CAPITALIZED_SINGULARCommandUseCase):
    """NAME_CAPITALIZED_SINGULARCommandUseCaseImpl implements a command usecases related NAME_CAPITALIZED_SINGULAR
    entity."""

    def __init__(
        self,
        uow: NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork,
    ):
        self.uow: NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork = uow

    def create_NAME_LOWER_SINGULAR(self, data: NAME_CAPITALIZED_SINGULARCreateModel) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        try:
            NAME_LOWER_SINGULAR = NAME_CAPITALIZED_SINGULAR(
                id=None,
            )
            created_NAME_LOWER_SINGULAR = self.uow.NAME_LOWER_SINGULAR_repository.create(NAME_LOWER_SINGULAR)
            self.uow.commit()

        except Exception:
            self.uow.rollback()
            raise

        return NAME_CAPITALIZED_SINGULARReadModel.from_entity(cast(NAME_CAPITALIZED_SINGULAR, created_NAME_LOWER_SINGULAR))

    def update_NAME_LOWER_SINGULAR(
        self, id: str, data: NAME_CAPITALIZED_SINGULARUpdateModel
    ) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
        try:
            existing_NAME_LOWER_SINGULAR = self.uow.NAME_LOWER_SINGULAR_repository.find_by_id(id)
            if existing_NAME_LOWER_SINGULAR is None:
                raise NAME_CAPITALIZED_SINGULARNotFoundError

            NAME_LOWER_SINGULAR = NAME_CAPITALIZED_SINGULAR(
                id=int(id),
            )

            self.uow.NAME_LOWER_SINGULAR_repository.update(NAME_LOWER_SINGULAR)
            self.uow.commit()

            updated_NAME_LOWER_SINGULAR = self.uow.NAME_LOWER_SINGULAR_repository.find_by_id(id)
        except Exception:
            self.uow.rollback()
            raise

        return NAME_CAPITALIZED_SINGULARReadModel.from_entity(cast(NAME_CAPITALIZED_SINGULAR, updated_NAME_LOWER_SINGULAR))

    def delete_NAME_LOWER_SINGULAR_by_id(self, id: str):
        try:
            existing_NAME_LOWER_SINGULAR = self.uow.NAME_LOWER_SINGULAR_repository.find_by_id(id)
            if existing_NAME_LOWER_SINGULAR is None:
                raise NAME_CAPITALIZED_SINGULARNotFoundError

            self.uow.NAME_LOWER_SINGULAR_repository.delete_by_id(id)

            self.uow.commit()
        except Exception:
            self.uow.rollback()
            raise
