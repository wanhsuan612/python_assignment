from pydantic import BaseModel

class FinancialData(BaseModel):
    symbol: str
    date: str
    open_price: str
    close_price: str
    volume: str
