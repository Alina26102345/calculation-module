from backend.calculator import calculate_metrics


def test_calc():
    data = [10, 20, 30]
    result = calculate_metrics(data)

    assert result["sum"] == 60
    assert result["average"] == 20
