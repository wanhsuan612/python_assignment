from pydantic import BaseModel, Field


class Pagination(BaseModel):
    """Pagination information for a query response."""

    count: int = Field(..., description="The total number of items in the result set.")
    page: int = Field(..., description="The current page number in the pagination.")
    limit: int = Field(..., description="The maximum number of items to return per page.")
    pages: int = Field(..., description="The total number of pages available in the result set.")
