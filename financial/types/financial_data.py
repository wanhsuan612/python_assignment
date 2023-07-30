from pydantic import BaseModel
from datetime import date

class FinancialData(BaseModel):
    symbol: str
    date: date
    open_price: str
    close_price: str
    volume: str
