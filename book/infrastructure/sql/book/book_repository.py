from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.book import Book, BookRepository
from app.usecase.book import BookCommandUseCaseUnitOfWork

from .entity_dto import BookDTO


class BookRepositoryImpl(BookRepository):
    """BookRepositoryImpl implements CRUD operations related Book
    entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[Book]:
        try:
            book_dto = (
                self.session.query(BookDTO)
                .filter_by(id=id)
                .one()
            )
        except NoResultFound:
            return None
        except Exception:
            raise

        return book_dto.to_entity()

    def create(self, book: Book):
        book_dto = BookDTO.from_entity(
            book
        )
        try:
            self.session.add(book_dto)
        except Exception:
            raise

    def update(self, book: Book):
        book_dto = BookDTO.from_entity(book)
        try:
            _book = self.session.query(BookDTO).filter_by(
                id=book_dto.id
            ).one()
            _book.name = book_dto.name
        except Exception:
            raise

    def delete_by_id(self, id: str):
        try:
            _book = self.session.query(BookDTO).filter_by(id=id).one()
            _book.deleted = True
        except Exception:
            raise


class BookCommandUseCaseUnitOfWorkImpl(
    BookCommandUseCaseUnitOfWork
):
    def __init__(
        self,
        session: Session,
        book_repository: BookRepository,
    ):
        self.session: Session = session
        self.book_repository: BookRepository = book_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
