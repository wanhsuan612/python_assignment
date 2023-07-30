import math

from financial.models.financial_data import FinancialData

def cal_average(data: list[FinancialData] = []):
    average_op = 0
    average_cp = 0
    average_v = 0
    if len(data) > 0:
        op_list = [float(d.open_price) for d in data]
        cp_list = [float(d.close_price) for d in data]
        v_list = [int(d.volume) for d in data]
        average_op = round(sum(op_list) / len(op_list), 2)
        average_cp = round(sum(cp_list) / len(cp_list), 2)
        average_v = math.ceil(sum(v_list) / len(v_list))
    return average_op, average_cp, average_v
