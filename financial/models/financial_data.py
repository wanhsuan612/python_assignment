from sqlalchemy import Column, Date, Integer, String

from financial.config.database import Base


class FinancialData(Base):
    __tablename__ = "financial_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(Date, index=True)
    open_price = Column(String)
    close_price = Column(String)
    volume = Column(String)
