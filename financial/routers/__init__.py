from fastapi import APIRouter

from . import financial_data, statistic


router = APIRouter(prefix="/api")
router.include_router(financial_data.router)
router.include_router(statistic.router)

__all__ = ["router"]
