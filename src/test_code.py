from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size
import pytest


def test_text_to_duration_int():
    """
    Test if text_to_duration returns expected duration value
    with a non zero minute component    
    """
    input_val = "10:00"
    assert text_to_duration(input_val) == 10

def test_text_to_duration_float():
    """
    Tests if .....
    """
    input_val = "10:15"
    assert text_to_duration(input_val) == 10.25
    input_val = "10:20"
    assert text_to_duration(input_val) == pytest.approx(10.33333333333333)


@pytest.mark.parametrize("input_value, epected_result", [
    ("A;", 1),
    ("A; B;", 2),
    ])
def test_calculate_cew_size (input_value, expected_result):
    """
    Test that the amount of #FIXME
    """
    actual_result =  calculate_crew_size(input_value)
    assert actual_result == expected_result