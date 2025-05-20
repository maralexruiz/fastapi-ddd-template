import logging
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.interface_adapters.localize import AcceptedLanguage, _
from app.interface_adapters.security import ACLClient, AuthUser  # type: ignore
from app.domain.NAME_LOWER_SINGULAR import NAME_CAPITALIZED_SINGULARNotFoundError
from app.usecase.client import ClientQueryUseCase
from app.presentation.schema.NAME_LOWER_SINGULAR import ErrorMessageNAME_CAPITALIZED_SINGULARNotFound
from app.usecase.NAME_LOWER_SINGULAR import (
    NAME_CAPITALIZED_SINGULARReadModel,
    NAME_CAPITALIZED_SINGULARCreateModel,
    NAME_CAPITALIZED_SINGULARUpdateModel,
    NAME_CAPITALIZED_SINGULARQueryUseCase,
    NAME_CAPITALIZED_SINGULARCommandUseCase
)
from app.interface_adapters.session.session_manager import (
    NAME_LOWER_SINGULAR_query_usecase,
    NAME_LOWER_SINGULAR_command_usecase,
    client_query_usecase
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
    response_model=List[NAME_CAPITALIZED_SINGULARReadModel],
)
async def get_NAME_LOWER_PLURAL(
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='allow_any'))],
    lang: Annotated[str, Depends(AcceptedLanguage())],
    NAME_LOWER_SINGULAR_query_usecase: NAME_CAPITALIZED_SINGULARQueryUseCase = Depends(
        NAME_LOWER_SINGULAR_query_usecase
    )
):
    try:
        NAME_LOWER_PLURAL = NAME_LOWER_SINGULAR_query_usecase.fetch_NAME_LOWER_PLURAL()
    except Exception as err:
        logger.error(err, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return NAME_LOWER_PLURAL


@router.get(
    "/{NAME_LOWER_SINGULAR_id}",
    response_model=NAME_CAPITALIZED_SINGULARReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageNAME_CAPITALIZED_SINGULARNotFound,
        },
    },
)
async def get_NAME_LOWER_SINGULAR(
    NAME_LOWER_SINGULAR_id: str,
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='allow_any'))],
    lang: Annotated[str, Depends(AcceptedLanguage())],
    NAME_LOWER_SINGULAR_query_usecase: NAME_CAPITALIZED_SINGULARQueryUseCase = Depends(
        NAME_LOWER_SINGULAR_query_usecase
    )
):
    try:
        NAME_LOWER_SINGULAR = NAME_LOWER_SINGULAR_query_usecase.fetch_NAME_LOWER_SINGULAR_by_id(
            NAME_LOWER_SINGULAR_id
        )
    except NAME_CAPITALIZED_SINGULARNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_(lang, err.i18n),
        )
    except Exception as err:
        logger.error(err, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return NAME_LOWER_SINGULAR


@router.post(
    "/",
    response_model=NAME_CAPITALIZED_SINGULARReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_NAME_LOWER_SINGULAR(
    data: NAME_CAPITALIZED_SINGULARCreateModel,
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='admin'))],
    NAME_LOWER_SINGULAR_command_usecase: NAME_CAPITALIZED_SINGULARCommandUseCase = Depends(
        NAME_LOWER_SINGULAR_command_usecase
    ),
    client_query_usecase: ClientQueryUseCase = Depends(
        client_query_usecase
    ),
):
    try:
        product = NAME_LOWER_SINGULAR_command_usecase.create_NAME_LOWER_SINGULAR(
            data,
            current_user,
            client_query_usecase,
        )
    except Exception as err:
        logger.error(err, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return product


@router.put(
    "/{NAME_LOWER_SINGULAR_id}",
    response_model=NAME_CAPITALIZED_SINGULARReadModel,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageNAME_CAPITALIZED_SINGULARNotFound,
        },
    },
)
async def update_NAME_LOWER_SINGULAR(
    NAME_LOWER_SINGULAR_id: str,
    data: NAME_CAPITALIZED_SINGULARUpdateModel,
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='admin'))],
    NAME_LOWER_SINGULAR_command_usecase: NAME_CAPITALIZED_SINGULARCommandUseCase = Depends(
        NAME_LOWER_SINGULAR_command_usecase
    ),
):
    try:
        updated_NAME_LOWER_SINGULAR = NAME_LOWER_SINGULAR_command_usecase.update_NAME_LOWER_SINGULAR(
            NAME_LOWER_SINGULAR_id,
            data,
            current_user,
        )
    except NAME_CAPITALIZED_SINGULARNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return updated_NAME_LOWER_SINGULAR


@router.delete(
    "/{NAME_LOWER_SINGULAR_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageNAME_CAPITALIZED_SINGULARNotFound,
        },
    },
)
async def delete_NAME_LOWER_SINGULAR(
    NAME_LOWER_SINGULAR_id: str,
    current_user: Annotated[AuthUser, Depends(ACLClient(rule='admin'))],
    NAME_LOWER_SINGULAR_command_usecase: NAME_CAPITALIZED_SINGULARCommandUseCase = Depends(
        NAME_LOWER_SINGULAR_command_usecase
    ),
):
    try:
        NAME_LOWER_SINGULAR_command_usecase.delete_NAME_LOWER_SINGULAR_by_id(NAME_LOWER_SINGULAR_id)
    except NAME_CAPITALIZED_SINGULARNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
