from typing import cast, Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.domain.book import Book


class BookReadModel(BaseModel):
    """BookReadModel represents data structure as a read model."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(examples=[23632])
    example_field: str = Field(examples=["Lore ipsum"])

    @staticmethod
    def from_entity(book: Book) -> "BookReadModel":
        return BookReadModel(
            id=book.id,
            example_field=book.example_field,
            created_at=cast(datetime, book.created_at),
        )
