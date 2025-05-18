from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.infrastructure.sql.database import SessionLocal

# Book
from app.domain.book import (
    BookRepository
)
from app.infrastructure.sql.book import (
    BookRepositoryImpl,
    BookCommandUseCaseUnitOfWorkImpl,
    BookQueryServiceImpl
)
from app.usecase.book import (
    BookQueryUseCase,
    BookQueryUseCaseImpl,
    BookQueryService,
    BookCommandUseCase,
    BookCommandUseCaseImpl,
    BookCommandUseCaseUnitOfWork
)


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# Book


def book_query_usecase(
    session: Session = Depends(get_session)
) -> BookQueryUseCase:
    book_query_service: BookQueryService = BookQueryServiceImpl(session)
    return BookQueryUseCaseImpl(book_query_service)


def book_command_usecase(
    session: Session = Depends(get_session)
) -> BookCommandUseCase:
    book_repository: BookRepository = BookRepositoryImpl(session)
    uow: BookCommandUseCaseUnitOfWork = BookCommandUseCaseUnitOfWorkImpl(
        session,
        book_repository=book_repository,
    )
    return BookCommandUseCaseImpl(uow)
