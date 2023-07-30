from sqlalchemy import Column, Date, Float, Integer, String

from financial.config.database import Base


class FinancialData(Base):
    __tablename__ = "financial_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    date = Column(Date, index=True)
    open_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)
