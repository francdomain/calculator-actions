from simple_calculator import add, sub, mul, div

def test_add():
    assert add(5, 7) == 12

def test_sub():
    assert sub(18, 7) == 11

def test_mul():
    assert mul(2, 11) == 22

def test_div():
    assert div(40, 8) == 5