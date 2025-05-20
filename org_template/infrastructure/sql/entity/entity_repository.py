from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULAR, NAME_CAPITALIZED_SINGULARRepository
from app.usecase.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork

from .NAME_LOWER_SINGULAR_dto import NAME_CAPITALIZED_SINGULARDTO


class NAME_CAPITALIZED_SINGULARRepositoryImpl(NAME_CAPITALIZED_SINGULARRepository):
    """NAME_CAPITALIZED_SINGULARRepositoryImpl implements CRUD operations related NAME_CAPITALIZED_SINGULAR
    entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[NAME_CAPITALIZED_SINGULAR]:
        try:
            NAME_LOWER_SINGULAR_dto = (
                self.session.query(NAME_CAPITALIZED_SINGULARDTO)
                .filter_by(id=id)
                .one()
            )
        except NoResultFound:
            return None
        except Exception:
            raise

        return NAME_LOWER_SINGULAR_dto.to_entity()

    def create(self, NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR):
        NAME_LOWER_SINGULAR_dto = NAME_CAPITALIZED_SINGULARDTO.from_entity(
            NAME_LOWER_SINGULAR
        )
        try:
            self.session.add(NAME_LOWER_SINGULAR_dto)
        except Exception:
            raise

    def update(self, NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR):
        NAME_LOWER_SINGULAR_dto = NAME_CAPITALIZED_SINGULARDTO.from_entity(NAME_LOWER_SINGULAR)
        try:
            _NAME_LOWER_SINGULAR = self.session.query(NAME_CAPITALIZED_SINGULARDTO).filter_by(
                id=NAME_LOWER_SINGULAR_dto.id
            ).one()
            _NAME_LOWER_SINGULAR.name = NAME_LOWER_SINGULAR_dto.name
        except Exception:
            raise

    def delete_by_id(self, id: str):
        try:
            _NAME_LOWER_SINGULAR = self.session.query(NAME_CAPITALIZED_SINGULARDTO).filter_by(id=id).one()
            _NAME_LOWER_SINGULAR.deleted = True
        except Exception:
            raise


class NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWorkImpl(
    NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork
):
    def __init__(
        self,
        session: Session,
        NAME_LOWER_SINGULAR_repository: NAME_CAPITALIZED_SINGULARRepository,
    ):
        self.session: Session = session
        self.NAME_LOWER_SINGULAR_repository: NAME_CAPITALIZED_SINGULARRepository = NAME_LOWER_SINGULAR_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
