from functools import lru_cache
from sqlalchemy.orm.query import Query

from financial.config.database import SessionLocal
from financial.models.financial_data import FinancialData
from financial.utils.exceptions import SymbolNotFound, DateNotFound

@lru_cache()
def get_financial_data(start_date=None, end_date=None, symbol=None):
    session = SessionLocal()
    _query = session.query(FinancialData)

    if symbol:
        _query = _filter_symbol(_query, symbol)
    if start_date:
        _query = _filter_start_date(_query, start_date)
    if end_date:
        _query = _filter_end_date(_query, end_date)

    data = _query.all()
    return data


def _filter_symbol(query: Query, value):
    _query = query.filter(FinancialData.symbol == value)
    _d = _query.all()
    if len(_d) == 0:
        raise SymbolNotFound(symbol=value)
    return _query


def _filter_start_date(query: Query, value):
    _query = query.filter(FinancialData.date >= value)
    _d = _query.all()
    if len(_d) == 0:
        start, end = get_valid_dates(query=query)
        raise DateNotFound(start=start, end=end)
    return _query


def _filter_end_date(query: Query, value):
    _query = query.filter(FinancialData.date <= value)
    _d = _query.all()
    if len(_d) == 0:
        start, end = get_valid_dates(query=query)
        raise DateNotFound(start=start, end=end)
    return _query


def get_valid_dates(query: Query):
    row_with_min_date = query.order_by(FinancialData.date).first()
    row_with_max_date = query.order_by(FinancialData.date.desc()).first()
    return row_with_min_date.date, row_with_max_date.date
