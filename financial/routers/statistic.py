from fastapi import APIRouter


# from financial.services.financial import get_financial

router = APIRouter(prefix="/statistic", tags=["statistic"])


@router.get("/")
def statistic():
    return {}
