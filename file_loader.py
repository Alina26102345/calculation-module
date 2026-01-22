import json
from errors import DataError


def load_from_uploaded_file(file_storage):
    try:
        data = json.load(file_storage)

        if "values" not in data:
            raise DataError("В файле нет поля 'values'")

        if not isinstance(data["values"], list):
            raise DataError("'values' должно быть списком")

        return data["values"]

    except json.JSONDecodeError:
        raise DataError("Файл не является корректным JSON")

