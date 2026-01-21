from flask import Flask, render_template, request
from calculator import calculate_metrics
from file_loader import load_from_file
from errors import DataError

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            mode = request.form.get("mode")

            if mode == "file":
                values = load_from_file("../data/input.json")

            else:
                raw = request.form.get("numbers")
                values = [float(x) for x in raw.split(",")]

            result = calculate_metrics(values)

        except DataError as e:
            error = str(e)
        except Exception:
            error = "Неизвестная ошибка"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
