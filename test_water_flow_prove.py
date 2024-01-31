from water_flow_prove import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi
import pytest

def test_water_column_height():
    # Test cases for water_column_height
    assert water_column_height(10, 5) == 5
    assert water_column_height(15, 10) == 5
    assert water_column_height(20, 18) == 2

def test_pressure_gain_from_water_height():
    # Test cases for pressure_gain_from_water_height
    assert pressure_gain_from_water_height(5) == 48.944990149999995
    assert pressure_gain_from_water_height(10) == 97.88998029999999
    assert pressure_gain_from_water_height(2) == 19.57799606

def test_pressure_loss_from_pipe():
    # Test cases for pressure_loss_from_pipe
    assert pressure_loss_from_pipe(0.1, 10, 0.02, 1) == 0.9982000000000001
    assert pressure_loss_from_pipe(0.15, 15, 0.018, 1.5) == 2.021355
    assert pressure_loss_from_pipe(0.2, 8, 0.015, 2) == 1.19784

def test_pressure_loss_from_fittings():
    # Test cases for pressure_loss_from_fittings
    assert pressure_loss_from_fittings(0.00, 3) == 0.000
    assert pressure_loss_from_fittings(1.65, 0) == 0.000
    assert pressure_loss_from_fittings(1.65, 2) == -0.10870398
    assert pressure_loss_from_fittings(1.75, 2) == -0.12227950000000001
    assert pressure_loss_from_fittings(1.75, 5) == -0.30569875

def test_reynolds_number():
    # Test cases for reynolds_number
    assert reynolds_number(0.048692, 0.00) == 0
    assert reynolds_number(0.048692, 1.65) == 80069.07424121405
    assert reynolds_number(0.048692, 1.75) == 84921.74540734824
    assert reynolds_number(0.28687, 1.65) == 471728.73013178905
    assert reynolds_number(0.28687, 1.75) == 500318.3501397763

def test_pressure_loss_from_pipe_reduction():
    # Test cases for pressure_loss_from_pipe_reduction
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == 0.000
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == -0.1358800945426303
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == -0.15284950178779946

def test_kPa_to_psi_conversion():
    # Test cases for kPa to psi conversion
    assert kPa_to_psi(100) == 14.503773773375 
    assert kPa_to_psi(200) == 29.00754754675
    assert kPa_to_psi(300) == 43.511321320125
    # Add more test cases as needed

if __name__ == '__main__':
    # Run all the test functions
    pytest.main(["-v", "--tb=line", "-rN", __file__])
