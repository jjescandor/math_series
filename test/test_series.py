from factorial.series import fibonacci, lucas, sum_series

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_two():
    assert fibonacci(2) == 1


def test_fibonacci_five():
    assert fibonacci(5) == 5


def test_fibonacci_eight():
    assert fibonacci(8) == 21


def test_lucas_one():
    assert lucas(1) == 1


def test_lucas_two():
    assert lucas(2) == 3


def test_lucas_five():
    assert lucas(5) == 11


def test_lucas_eight():
    assert lucas(8) == 47


def test_sum_series_fibonacci_one():
    assert sum_series(1) == 1


def test_sum_series_fibonacci_two():
    assert sum_series(1) == 1


def test_sum_series_fibonacci_five():
    assert sum_series(5) == 5


def test_sum_series_fibonacci_eight():
    assert sum_series(8) == 21

def test_sum_series_lucas_one():
    assert sum_series(1,2,1) == 1


def test_sum_series_lucas_two():
    assert sum_series(2,2,1) == 3


def test_sum_series_lucas_five():
    assert sum_series(5,2,1) == 11


def test_sum_series_lucas_eight():
    assert sum_series(8,2,1) == 47