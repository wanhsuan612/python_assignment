from sqlalchemy import Column, Date, Integer, String
from financial.config.database import Base

class FinancialData(Base):
    """Represents financial data for a specific stock symbol.

    This class is used to model the financial data related to a specific stock symbol,
    including information like the opening price, closing price, and trading volume for a given date.

    Attributes:
        id (Integer): The unique identifier for the financial data record. It serves as the primary key.
        symbol (String): The stock symbol, e.g., "AAPL" for Apple Inc.
        date (Date): The date for the financial data.
        open_price (String): The opening price of the stock on the given date.
        close_price (String): The closing price of the stock on the given date.
        volume (String): The trading volume of the stock on the given date.

    Example:
        >>> financial_data = FinancialData(
        ...     symbol="AAPL",
        ...     date="2022-01-01",
        ...     open_price="150.00",
        ...     close_price="145.00",
        ...     volume="1000000"
        ... )
    """

    __tablename__ = "financial_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(Date, index=True)
    open_price = Column(String)
    close_price = Column(String)
    volume = Column(String)
