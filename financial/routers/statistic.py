from fastapi import APIRouter


from financial.services.financial_data import get_financial_data
from financial.services.statistics import cal_average
from financial.types.response import StatisticResponse

router = APIRouter(prefix="/statistics", tags=["statistic"])


@router.get("/", response_model=StatisticResponse, response_model_exclude_none=False)
def average(start_date: str, end_date: str, symbol: str):
    err_msg = ""
    try:
        data = get_financial_data(start_date=start_date, end_date=end_date, symbol=symbol)
    except Exception as e:
        err_msg = str(e)
    finally:
        average_op, average_cp, average_v = cal_average(data)
        return {
            "data": {
                "start_date": start_date,
                "end_date": end_date,
                "symbol": symbol,
                "average_daily_open_price": average_op,
                "average_daily_close_price": average_cp,
                "average_daily_volume": average_v
            },
            "info": {
                "error": err_msg
            }
        }
