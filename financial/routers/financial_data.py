from datetime import date

from fastapi import APIRouter

from financial.services.financial_data import get_financial_data
from financial.types.response import FinancialDataResponse
from financial.utils.common import pagination
from financial.utils.exceptions import InvalidDateZone


router = APIRouter(prefix="/financial_data", tags=["financial_data"])


@router.get("", response_model=FinancialDataResponse, response_model_exclude_none=False)
def financial(start_date: date = None, end_date: date = None, symbol: str = None, limit: int = 10, page: int = 1):
    err = ""
    data = []
    try:
        if start_date and end_date:
            if start_date > end_date:
                raise InvalidDateZone(start=start_date, end=end_date)
        data = get_financial_data(start_date=start_date, end_date=end_date, symbol=symbol)
    except Exception as e:
        err = str(e)
    finally:
        count, total_pages, paginated_data = pagination(page, limit, data)
        return {
            "data": paginated_data,
            "pagination": {"count": count, "page": page, "limit": limit, "pages": total_pages},
            "info": {"error": err},
        }
