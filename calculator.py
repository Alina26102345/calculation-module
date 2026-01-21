from errors import DataError


def calculate_metrics(values: list):
    if len(values) == 0:
        raise DataError("Список пуст")

    for v in values:
        if not isinstance(v, (int, float)):
            raise DataError("Все значения должны быть числами")

    total = sum(values)
    avg = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return {
        "sum": total,
        "average": avg,
        "max": maximum,
        "min": minimum
    }
