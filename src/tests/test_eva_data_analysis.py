from eva_data_analysis import text_to_duration

def test_text_to_duration_int():
    input_val = "10:00"
    assert text_to_duration(input_val) == 10

def test_text_to_duration_float():
    input_val = "10:15"
    assert text_to_duration(input_val) == 10.25
    input_val = "10:20"
    assert abs(text_to_duration(input_val) - 10.33333333333333) < 1e-5 # test if they are close enough by using a tolerance

