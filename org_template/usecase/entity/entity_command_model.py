from pydantic import BaseModel, Field


class NAME_CAPITALIZED_SINGULARCreateModel(BaseModel):
    """NAME_CAPITALIZED_SINGULARCreateModel represents a write model to create a NAME_LOWER_SINGULAR."""

    example_field: str = Field(examples=["Lore ipsum"])


class NAME_CAPITALIZED_SINGULARUpdateModel(BaseModel):
    """NAME_CAPITALIZED_SINGULARUpdateModel represents a write model to update a NAME_LOWER_SINGULAR."""

    example_field: str = Field(examples=["Lore ipsum"])
