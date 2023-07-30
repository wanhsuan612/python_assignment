from fastapi import APIRouter

from financial.services.financial_data import get
from financial.utils.common import pagination
from financial.types.response import FinancialDataResponse


router = APIRouter(prefix="/financial_data", tags=["financial_data"])


@router.get("/", response_model=FinancialDataResponse, response_model_exclude_none=False)
def financial(start_date: str = None, end_date: str = None, symbol: str = None, limit: int = 10, page: int = 1):
    err_msg = ""
    data = []
    try:
        data = get(start_date=start_date, end_date=end_date, symbol=symbol)
    except Exception as e:
        err_msg = e
    finally:
        count, total_pages, paginated_data = pagination(page, limit, data)
        return {
            "data": paginated_data,
            "pagination": {
                "count": count,
                "page": page,
                "limit": limit,
                "pages": total_pages
            },
            "info": {
                "error": err_msg
            }
        }
