import os
from flask import Flask, render_template, request

from calculator import calculate_metrics
from file_loader import load_from_uploaded_file
from errors import DataError


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "frontend", "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            mode = request.form.get("mode")

            # -------- ЗАГРУЗКА ФАЙЛА --------
            if mode == "file":
                if "file" not in request.files:
                    raise DataError("Файл не выбран")

                file = request.files["file"]

                if file.filename == "":
                    raise DataError("Файл не выбран")

                values = load_from_uploaded_file(file)

            # -------- ВВОД ВРУЧНУЮ --------
            else:
                raw = request.form.get("numbers")

                if not raw:
                    raise DataError("Строка с числами пустая")

                try:
                    values = [float(x.strip()) for x in raw.split(",")]
                except ValueError:
                    raise DataError("Введите числа через запятую, например: 10,20,30")

            result = calculate_metrics(values)

        except DataError as e:
            error = str(e)
        except Exception:
            error = "Внутренняя ошибка сервера"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)

