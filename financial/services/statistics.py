import math

from financial.models.financial_data import FinancialData


def cal_average(data: list[FinancialData] = []):
    """
    Calculate the average open price, close price, and volume from a list of financial data.

    Args:
        data (list[FinancialData], optional): A list of FinancialData objects containing the
                                             open price, close price, and volume. Defaults to an empty list.

    Returns:
        tuple: A tuple containing three floats, representing the average open price (rounded to two decimal places),
               the average close price (rounded to two decimal places), and the average volume (rounded up).

    """
    if not data:
        return 0, 0, 0

    total_op, total_cp, total_v = 0, 0, 0
    for d in data:
        total_op += float(d.open_price)
        total_cp += float(d.close_price)
        total_v += int(d.volume)

    n = len(data)
    average_op = round(total_op / n, 2)
    average_cp = round(total_cp / n, 2)
    average_v = math.ceil(total_v / n)

    return average_op, average_cp, average_v
