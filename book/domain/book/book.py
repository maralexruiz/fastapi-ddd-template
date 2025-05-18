from typing import Optional


class NAME_CAPITALIZED_SINGULA:
    """NAME_CAPITALIZED_SINGULA represents your collection of entites as an entity."""

    def __init__(
        self,
        id: Optional[int],
    ):
        self.id: Optional[int] = id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, NAME_CAPITALIZED_SINGULA):
            return self.id == o.id
        return False
