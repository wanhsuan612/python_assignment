from functools import lru_cache

from sqlalchemy.orm.query import Query

from financial.config.database import SessionLocal
from financial.models.financial_data import FinancialData
from financial.utils.exceptions import DateNotFound, SymbolNotFound


@lru_cache()
def get_financial_data(start_date=None, end_date=None, symbol=None):
    """Retrieve financial data based on the provided filtering criteria.

    This function queries the FinancialData table and applies optional filters
    for symbol, start_date, and end_date.

    Args:
        start_date (date, optional): The starting date of the data retrieval (inclusive).
        end_date (date, optional): The ending date of the data retrieval (inclusive).
        symbol (str, optional): The stock symbol to filter by.

    Returns:
        list[FinancialData]: A list of FinancialData objects that match the filtering criteria.
    """
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
    """Filter the query based on a stock symbol.

    Args:
        query (Query): The initial query object.
        value (str): The stock symbol to filter by.

    Returns:
        Query: A modified query object filtered by the stock symbol.

    Raises:
        SymbolNotFound: If no data is found for the given symbol.
    """
    _query = query.filter(FinancialData.symbol == value)
    _d = _query.all()
    # If no data, raise SymbolNotFound
    if len(_d) == 0:
        raise SymbolNotFound(symbol=value)
    return _query


def _filter_start_date(query: Query, value):
    """Filter the query based on the start date.

    Args:
        query (Query): The initial query object.
        value (date): The starting date to filter by.

    Returns:
        Query: A modified query object filtered by the start date.

    Raises:
        DateNotFound: If no data is found for the given start date.
    """
    _query = query.filter(FinancialData.date >= value)
    _d = _query.all()
    # If no data, get the available min and max date for searching, raise DateNotFound
    if len(_d) == 0:
        start, end = get_valid_dates(query=query)
        raise DateNotFound(start=start, end=end)
    return _query


def _filter_end_date(query: Query, value):
    """Filter the query based on the end date.

    Args:
        query (Query): The initial query object.
        value (date): The ending date to filter by.

    Returns:
        Query: A modified query object filtered by the end date.

    Raises:
        DateNotFound: If no data is found for the given end date.
    """
    _query = query.filter(FinancialData.date <= value)
    _d = _query.all()
    # If no data, get the available min and max date for searching, raise DateNotFound
    if len(_d) == 0:
        start, end = get_valid_dates(query=query)
        raise DateNotFound(start=start, end=end)
    return _query


def get_valid_dates(query: Query):
    """Retrieve the minimum and maximum dates from the FinancialData table.

    Args:
        query (Query): The initial query object.

    Returns:
        Tuple[date, date]: A tuple containing the minimum and maximum dates present in the FinancialData table.
    """
    row_with_min_date = query.order_by(FinancialData.date).first()
    row_with_max_date = query.order_by(FinancialData.date.desc()).first()
    return row_with_min_date.date, row_with_max_date.date
