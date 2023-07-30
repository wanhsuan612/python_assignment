from datetime import date

from fastapi import APIRouter

from financial.services.financial_data import get_financial_data
from financial.services.statistics import cal_average
from financial.types.response import StatisticResponse
from financial.utils.exceptions import InvalidDateZone


router = APIRouter(prefix="/statistics", tags=["statistic"])


@router.get("", response_model=StatisticResponse, response_model_exclude_none=False)
def average(start_date: date, end_date: date, symbol: str):
    """Calculate and retrieve average daily open price, close price, and volume for a given symbol and date range.

    This endpoint provides the ability to fetch average daily open price, close price, and volume
    for a specified stock symbol between a given start and end date. If the start_date is greater
    than the end_date, it raises an InvalidDateZone error.
    """
    err = ""
    data = []
    try:
        if start_date > end_date:
            raise InvalidDateZone(start=start_date, end=end_date)
        data = get_financial_data(start_date=start_date, end_date=end_date, symbol=symbol)
    except Exception as e:
        err = str(e)
    finally:
        average_op, average_cp, average_v = cal_average(data)
        return {
            "data": {
                "start_date": start_date,
                "end_date": end_date,
                "symbol": symbol,
                "average_daily_open_price": average_op,
                "average_daily_close_price": average_cp,
                "average_daily_volume": average_v,
            },
            "info": {"error": err},
        }
