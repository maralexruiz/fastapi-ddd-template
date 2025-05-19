from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.infrastructure.sql.database import SessionLocal

# NAME_CAPITALIZED_SINGULAR
from app.domain.NAME_LOWER_SINGULAR import (
    NAME_CAPITALIZED_SINGULARRepository
)
from app.infrastructure.sql.NAME_LOWER_SINGULAR import (
    NAME_CAPITALIZED_SINGULARRepositoryImpl,
    NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWorkImpl,
    NAME_CAPITALIZED_SINGULARQueryServiceImpl
)
from app.usecase.NAME_LOWER_SINGULAR import (
    NAME_CAPITALIZED_SINGULARQueryUseCase,
    NAME_CAPITALIZED_SINGULARQueryUseCaseImpl,
    NAME_CAPITALIZED_SINGULARQueryService,
    NAME_CAPITALIZED_SINGULARCommandUseCase,
    NAME_CAPITALIZED_SINGULARCommandUseCaseImpl,
    NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork
)


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# NAME_CAPITALIZED_SINGULAR


def NAME_LOWER_SINGULAR_query_usecase(
    session: Session = Depends(get_session)
) -> NAME_CAPITALIZED_SINGULARQueryUseCase:
    NAME_LOWER_SINGULAR_query_service: NAME_CAPITALIZED_SINGULARQueryService = NAME_CAPITALIZED_SINGULARQueryServiceImpl(session)
    return NAME_CAPITALIZED_SINGULARQueryUseCaseImpl(NAME_LOWER_SINGULAR_query_service)


def NAME_LOWER_SINGULAR_command_usecase(
    session: Session = Depends(get_session)
) -> NAME_CAPITALIZED_SINGULARCommandUseCase:
    NAME_LOWER_SINGULAR_repository: NAME_CAPITALIZED_SINGULARRepository = NAME_CAPITALIZED_SINGULARRepositoryImpl(session)
    uow: NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWork = NAME_CAPITALIZED_SINGULARCommandUseCaseUnitOfWorkImpl(
        session,
        NAME_LOWER_SINGULAR_repository=NAME_LOWER_SINGULAR_repository,
    )
    return NAME_CAPITALIZED_SINGULARCommandUseCaseImpl(uow)
