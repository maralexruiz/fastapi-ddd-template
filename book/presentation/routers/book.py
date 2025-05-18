import logging
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.interface_adapters.localize import AcceptedLanguage, _
from app.interface_adapters.security import ACLClient, AuthUser  # type: ignore
from app.domain.book import BookNotFoundError
from app.presentation.schema.entity import ErrorMessageBookNotFound
from app.usecase.book import (
    BookReadModel,
    BookQueryUseCase
)
from app.interface_adapters.session.session_manager import (
    book_query_usecase
)

logger = logging.getLogger(__name__)

router = APIRouter()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.get(
    "/",
    response_model=List[BookReadModel],
)
async def get_books(
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='allow_any'))],
    lang: Annotated[str, Depends(AcceptedLanguage())],
    book_query_usecase: BookQueryUseCase = Depends(
        book_query_usecase
    )
):
    try:
        books = book_query_usecase.fetch_books()
    except Exception as err:
        logger.error(err, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return books


@router.get(
    "/{book_id}",
    response_model=BookReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageBookNotFound,
        },
    },
)
async def get_book(
    book_id: str,
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='allow_any'))],
    lang: Annotated[str, Depends(AcceptedLanguage())],
    book_query_usecase: BookQueryUseCase = Depends(
        book_query_usecase
    )
):
    try:
        book = book_query_usecase.fetch_book_by_id(
            book_id
        )
    except BookNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_(lang, err.i18n),
        )
    except Exception as err:
        logger.error(err, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return book
