import json
from errors import DataError


def load_from_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "values" not in data:
            raise DataError("Нет поля 'values'")

        if not isinstance(data["values"], list):
            raise DataError("'values' должно быть списком")

        return data["values"]

    except FileNotFoundError:
        raise DataError("Файл не найден")
    except json.JSONDecodeError:
        raise DataError("Ошибка формата JSON")
