from pydantic import BaseModel
from datetime import date

class Statistic(BaseModel):
    start_date: date
    end_date: date
    symbol: str
    average_daily_open_price: float
    average_daily_close_price: float
    average_daily_volume: int
