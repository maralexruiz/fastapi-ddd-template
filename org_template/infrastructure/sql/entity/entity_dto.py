from sqlalchemy import Column, Integer

from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULAR
from app.infrastructure.sql.database import Base
from app.usecase.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULARReadModel


class NAME_CAPITALIZED_SINGULARDTO(Base):
    """NAME_CAPITALIZED_SINGULARDTO is a data transfer object associated with NAME_LOWER_SINGULAR entity."""

    __tablename__ = "NAME_LOWER_SINGULAR"

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)

    def to_entity(self) -> NAME_CAPITALIZED_SINGULAR:
        return NAME_CAPITALIZED_SINGULAR(
            id=self.id,
        )

    def to_read_model(self) -> NAME_CAPITALIZED_SINGULARReadModel:
        return NAME_CAPITALIZED_SINGULARReadModel(
            id=self.id,
        )

    @staticmethod
    def from_entity(NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR) -> "NAME_CAPITALIZED_SINGULARDTO":
        return NAME_CAPITALIZED_SINGULARDTO(
            id=NAME_LOWER_SINGULAR.id,
        )
