from pydantic import BaseModel, Field

from financial.types.financial_data import FinancialData
from financial.types.pagination import Pagination
from financial.types.statistic import Statistic


class Info(BaseModel):
    """Error information."""

    error: str = Field("", description="An error message, if any.")


class BaseResponse(BaseModel):
    """A base response model for the API response."""

    data: list | dict = Field(..., description="The response data, either as a list or a dictionary.")
    info: Info = Field(..., description="Additional information such as error messages.")


class FinancialDataResponse(BaseResponse):
    """Response model for retrieving financial data."""

    data: list[FinancialData] = Field([], description="A list of financial data objects.")
    pagination: Pagination = Field(..., description="Pagination details.")


class StatisticResponse(BaseResponse):
    """Response model for retrieving statistical data."""

    data: Statistic = Field(..., description="A statistic object containing statistical details.")
