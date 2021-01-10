from calculator import add

def test_empty_string():
    assert add('') == 0

def test_single_digit():
    assert add('0') == 0
    assert add('9') == 9