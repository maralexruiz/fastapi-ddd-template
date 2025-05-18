from pydantic import BaseModel, Field


class BookCreateModel(BaseModel):
    """BookCreateModel represents a write model to create a book."""

    example_field: str = Field(examples=["Lore ipsum"])

class BookUpdateModel(BaseModel):
    """BookUpdateModel represents a write model to update a book."""

    example_field: str = Field(examples=["Lore ipsum"])