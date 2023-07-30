from pydantic import BaseModel

class Pagination(BaseModel):
    count: int = 0
    page: int
    limit: int
    pages: int = 0