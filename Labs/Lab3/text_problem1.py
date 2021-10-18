from problem1 import splited_amount

def test_problem1():
    assert(splited_amount(100, 2, 0.18))
    assert(splited_amount(20, 5, 0.15))
    assert(splited_amount(50.66, 3, 0.18))