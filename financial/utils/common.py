import math


def pagination(page: int, limit: int, data: list):
    """Divides the given data into pages according to the provided page number and limit per page.

    This function returns the count of total items, the number of total pages, and the items
    for the requested page.

    Args:
        page (int): The requested page number.
        limit (int): The number of items per page.
        data (list): The list of data items to be paginated.

    Returns:
        count (int): The total number of items in the data.
        total_pages (int): The total number of pages.
        paginated_data (list): The items for the requested page.
    """
    count = len(data)
    if count == 0:
        return 0, 0, []

    total_pages = math.ceil(count / limit)
    start_index = (page - 1) * limit
    end_index = min(start_index + limit, count)  # Avoid indexing beyond the list
    paginated_data = data[start_index:end_index]

    return count, total_pages, paginated_data
