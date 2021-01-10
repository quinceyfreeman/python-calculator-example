from calculator import add

def test_empty_string():
    assert add('') == 0

def test_single_digit():
    assert add('0') == 0
    assert add('9') == 9

def test_two_digits_seperated_by_commas():
    assert add('1,1') == 2

def test_three_digits_seperated():
    assert add('42,-1,17') == 58

def test_two_digits_on_seperate_lines():
    assert add('17\n42') == 59

def test_multi_line_with_commas():
    assert add('1,2\n3,4\n42') == 52