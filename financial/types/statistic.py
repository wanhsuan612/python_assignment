from datetime import date

from pydantic import BaseModel, Field


class Statistic(BaseModel):
    """Represents statistical data for a given stock symbol over a specific date range."""

    start_date: date = Field(..., description="The starting date of the statistics period.")
    end_date: date = Field(..., description="The ending date of the statistics period.")
    symbol: str = Field(..., description="The stock symbol.")
    average_daily_open_price: float = Field(..., description="The average daily open price.")
    average_daily_close_price: float = Field(..., description="The average daily close price.")
    average_daily_volume: int = Field(..., description="The average daily trading volume.")
