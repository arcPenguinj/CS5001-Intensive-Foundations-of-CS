'''
Fall2020
CS 5001 HW3
Yici Zhu
it's the unitest for expenses.py
'''
from expenses import calculate_mileage
from expenses import get_reimbursement_amount
from expenses import get_actual_mileage_rate
from expenses import get_actual_trip_cost


def test_calculate_mileage():
    assert(calculate_mileage(50, 100) == 50)
    assert(calculate_mileage(25, 0) == 0)
    assert(calculate_mileage(0, 15) == 0)
    assert(calculate_mileage(-2, 100) == 0)
    assert(calculate_mileage(33, 46) == 13)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(30) == 17.25)
    assert(get_reimbursement_amount(66) == 37.95)
    assert(get_reimbursement_amount(22.5) == 12.94)
    assert(get_reimbursement_amount(0) == 0)
    assert(get_reimbursement_amount(28) == 16.1)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(28, 3.94) == 0.1407)
    assert(get_actual_mileage_rate(0, 3.94) == 0)
    assert(get_actual_mileage_rate(28, 0) == 0)
    assert(get_actual_mileage_rate(35, 2.94) == 0.084)
    assert(get_actual_mileage_rate(-2, 3.94) == 0)
    assert(get_actual_mileage_rate(28, -5) == 0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(10, 25, 28, 3.94) == 2.11)
    assert(get_actual_trip_cost(0, 25, 28, 3.94) == 0)
    assert(get_actual_trip_cost(10, 0, 28, 3.94) == 0)
    assert(get_actual_trip_cost(10, 25, 0, 3.94) == 0)
    assert(get_actual_trip_cost(10, 25, 28, 0) == 0)
    assert(get_actual_trip_cost(15.55, 28.33, 31.5, 3.55) == 1.44)
