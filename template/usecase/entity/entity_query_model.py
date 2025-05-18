from typing import cast, Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULAR


class NAME_CAPITALIZED_SINGULARReadModel(BaseModel):
    """NAME_CAPITALIZED_SINGULARReadModel represents data structure as a read model."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(examples=[23632])
    example_field: str = Field(examples=["Lore ipsum"])

    @staticmethod
    def from_entity(NAME_LOWER_SINGULAR: NAME_CAPITALIZED_SINGULAR) -> "NAME_CAPITALIZED_SINGULARReadModel":
        return NAME_CAPITALIZED_SINGULARReadModel(
            id=NAME_LOWER_SINGULAR.id,
            example_field=NAME_LOWER_SINGULAR.example_field,
            created_at=cast(datetime, NAME_LOWER_SINGULAR.created_at),
        )
