def test_add(a, b):
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(1000000000000000000, 2) == 1000000000000000002

def test_multiply(a, b):
    assert multiply(1, 1) == 1
    assert multiply(1, 2) == 2
    assert multiply(9, 2) == 18
    