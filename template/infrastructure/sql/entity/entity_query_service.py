from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULARQueryService, NAME_CAPITALIZED_SINGULARReadModel

from .NAME_LOWER_SINGULAR_dto import NAME_CAPITALIZED_SINGULARDTO


class NAME_CAPITALIZED_SINGULARQueryServiceImpl(NAME_CAPITALIZED_SINGULARQueryService):
    """NAME_CAPITALIZED_SINGULARQueryServiceImpl implements READ operations related NAME_CAPITALIZED_SINGULAR
    entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: int) -> Optional[NAME_CAPITALIZED_SINGULARReadModel]:
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

        return NAME_LOWER_SINGULAR_dto.to_read_model()

    def find_all(self) -> List[NAME_CAPITALIZED_SINGULARReadModel]:
        try:
            NAME_LOWER_SINGULAR_dtos = (
                self.session.query(NAME_CAPITALIZED_SINGULARDTO)
                .limit(100)
                .all()
            )
        except Exception:
            raise

        if len(NAME_LOWER_SINGULAR_dtos) == 0:
            return []

        return list(map(
            lambda NAME_LOWER_SINGULAR_dto: NAME_LOWER_SINGULAR_dto.to_read_model(), NAME_LOWER_SINGULAR_dtos)
        )
