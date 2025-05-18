from sqlalchemy import Column, Integer

from app.domain.book import Book
from app.infrastructure.sql.database import Base
from app.usecase.book import BookReadModel


class BookDTO(Base):
    """BookDTO is a data transfer object associated with book entity."""

    __tablename__ = "book"

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)

    def to_entity(self) -> Book:
        return Book(
            id=self.id,
        )

    def to_read_model(self) -> BookReadModel:
        return BookReadModel(
            id=self.id,
        )

    @staticmethod
    def from_entity(book: Book) -> "BookDTO":
        return BookDTO(
            id=book.id,
        )
