from pydantic import BaseModel, Field

from app.domain.NAME_LOWER_SINGULAR import (
    NAME_CAPITALIZED_SINGULARNotFoundError,
    NAME_CAPITALIZED_PLURALNotFoundError,
)


class ErrorMessageNAME_CAPITALIZED_SINGULARNotFound(BaseModel):
    detail: str = Field(examples=[NAME_CAPITALIZED_SINGULARNotFoundError.message])


class ErrorMessageNAME_CAPITALIZED_PLURALNotFound(BaseModel):
    detail: str = Field(examples=[NAME_CAPITALIZED_PLURALNotFoundError.message])
