from datetime import datetime
from functools import lru_cache

from financial.config.database import SessionLocal
from financial.models.financial_data import FinancialData

@lru_cache()
def get(start_date=None, end_date=None, symbol=None):
    session = SessionLocal()
    _query = session.query(FinancialData)
    if symbol:
        _query = _query.filter(FinancialData.symbol == symbol)
    if start_date:
        sd = datetime.strptime(start_date, "%Y-%m-%d")
        _query = _query.filter(FinancialData.date >= sd)
    if end_date:
        ed = datetime.strptime(end_date, "%Y-%m-%d")
        _query = _query.filter(FinancialData.date <= ed)

    data = _query.all()
    session.close()
    return data
