from pydantic import BaseModel, Field

from app.domain.book import (
    BookNotFoundError,
    BooksNotFoundError,
)


class ErrorMessageBookNotFound(BaseModel):
    detail: str = Field(examples=[BookNotFoundError.message])


class ErrorMessageBooksNotFound(BaseModel):
    detail: str = Field(examples=[BooksNotFoundError.message])
