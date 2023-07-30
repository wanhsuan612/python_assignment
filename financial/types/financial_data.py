from datetime import date as _date

from pydantic import BaseModel, Field


class FinancialData(BaseModel):
    """Represents a record of financial data for a particular stock symbol."""

    symbol: str = Field(..., description="The stock symbol.")
    date: _date = Field(..., description="The trading date.")
    open_price: str = Field(..., description="The opening price of the stock on the trading date.")
    close_price: str = Field(..., description="The closing price of the stock on the trading date.")
    volume: str = Field(..., description="The trading volume of the stock on the trading date.")
