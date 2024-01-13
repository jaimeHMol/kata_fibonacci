import pytest

from src.kata_fibonacci import fibonacci


def test_type_fibonacci_results():
    """ Test that the type returned by the Fibonacci function is the expected."""
    num_fibonacci = 2
    result = fibonacci(num_fibonacci)
    assert type(result) == list

def test_size_fibonacci_results():
    """ Test that the amount of elements on the list expected match the amount of
    Fibonacci numbers requested. """
    num_fibonacci = 4
    result = fibonacci(num_fibonacci)
    assert len(result) == num_fibonacci

def test_fibonacci_results():
    """ Test that the result has the expected numbers of the Fibonacci series. """
    num_fibonacci = 9
    result = fibonacci(num_fibonacci)
    expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert result == expected_result
    
def test_fibonacci_results_small_number():
    """ Test that the result has the expected numbers of the Fibonacci series when the
    Fibonacci number requested is small. """
    num_fibonacci = 2
    result = fibonacci(num_fibonacci)
    expected_result = [0, 1]
    assert result == expected_result

def test_fibonacci_results_negative_number():
    """ Test that the function correctly handles when a negative Fibonacci number is
     requested.  """
    num_fibonacci = -2
    with pytest.raises(ValueError):
        fibonacci(num_fibonacci)

def test_fibonacci_results_float_number():
    """ Test that the function correctly handles when a float Fibonacci number is
     requested.  """
    num_fibonacci = -0.1
    with pytest.raises(ValueError):
        fibonacci(num_fibonacci)