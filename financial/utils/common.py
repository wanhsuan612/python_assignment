import math

def pagination(page: int, limit: int, data: list):
    count = len(data)
    if count == 0:
        return 0, 0, []
    total_pages = math.ceil(len(data) / limit)
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_date = data[start_index:end_index]
    return count, total_pages, paginated_date
