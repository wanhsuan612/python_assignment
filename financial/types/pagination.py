from pydantic import BaseModel

class Pagination(BaseModel):
    count: int
    page: int
    limit: int
    pages: int