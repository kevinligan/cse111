from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
import pytest

def test_water_column_height():
    # Test case 1
    result_1 = water_column_height(0.0, 0.0)
    assert result_1 == 0.0, f"Test case 1 failed: expected 0.0, got {result_1}"

    # Test case 2
    result_2 = water_column_height(0.0, 10.0)
    assert result_2 == 7.5, f"Test case 2 failed: expected 7.5, got {result_2}"

    # Test case 3
    result_3 = water_column_height(25.0, 0.0)
    assert result_3 == 25.0, f"Test case 3 failed: expected 25.0, got {result_3}"

    # Test case 4
    result_4 = water_column_height(48.3, 12.8)
    assert result_4 == 57.9, f"Test case 4 failed: expected 57.9, got {result_4}"

def test_pressure_gain_from_water_height():
    # Test case 1
    result_1 = pressure_gain_from_water_height(0.0)
    assert abs(result_1 - 0.000) < 0.001, f"Test case 1 failed: expected 0.000, got {result_1}"

    # Test case 2
    result_2 = pressure_gain_from_water_height(30.2)
    assert abs(result_2 - 295.628) < 0.001, f"Test case 2 failed: expected 295.628, got {result_2}"

    # Test case 3
    result_3 = pressure_gain_from_water_height(50.0)
    assert abs(result_3 - 489.450) < 0.001, f"Test case 3 failed: expected 489.450, got {result_3}"

def test_pressure_loss_from_pipe():
    # Test case 1
    result_1 = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75)
    assert abs(result_1 - 0.000) < 0.001, f"Test case 1 failed: expected 0.000, got {result_1}"

    # Test case 2
    result_2 = pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75)
    assert abs(result_2 - 0.000) < 0.001, f"Test case 2 failed: expected 0.000, got {result_2}"

    # Test case 3
    result_3 = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00)
    assert abs(result_3 - 0.000) < 0.001, f"Test case 3 failed: expected 0.000, got {result_3}"

    # Test case 4
    result_4 = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75)
    assert abs(result_4 + 113.008) < 0.001, f"Test case 4 failed: expected -113.008, got {result_4}"

    # Test case 5
    result_5 = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65)
    assert abs(result_5 + 100.462) < 0.001, f"Test case 5 failed: expected -100.462, got {result_5}"

    # Test case 6
    result_6 = pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65)
    assert abs(result_6 + 61.576) < 0.001, f"Test case 6 failed: expected -61.576, got {result_6}"

    # Test case 7
    result_7 = pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65)
    assert abs(result_7 + 110.884) < 0.001, f"Test case 7 failed: expected -110.884, got {result_7}"

    # Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])