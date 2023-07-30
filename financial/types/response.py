from pydantic import BaseModel
from financial.types.financial_data import FinancialData
from financial.types.statistic import Statistic
from financial.types.pagination import Pagination

class Info(BaseModel):
    error: str = ""

class BaseResponse(BaseModel):
    data: list | dict
    info: Info

class FinancialDataResponse(BaseResponse):
    data: list[FinancialData] = []
    pagination: Pagination

class StatisticResponse(BaseResponse):
    data: Statistic
