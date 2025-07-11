# Test cases for the fibonacci_module.py file.
import pytest
from fibonacci_module import (
    fib_list,
    is_square,
    is_fibonacci,
    n_Binet,
    nearest_Binet_fib,
    make_saved_Fibonacci_file,
    get_nth_saved_Fibonacci_number
)


def test_fib_list():
    # Test with positive integers
    assert fib_list(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # Test with negative integers
    with pytest.raises(ValueError):
        fib_list(-1)
    # Test with non-integer values
    with pytest.raises(TypeError):
        fib_list(1.5)
    # Test with non-numeric values
    with pytest.raises(TypeError):
        fib_list("a")


def test_is_square():
    # Test with perfect squares
    assert is_square(16) == True
    # Test with non-perfect squares
    assert is_square(20) == False
    # Test with negative numbers
    assert is_square(-4) == False
    # Test with non-numeric values
    with pytest.raises(TypeError):
        is_square("a")


def test_is_fibonacci():
    # Test with Fibonacci numbers
    assert is_fibonacci(13) == True
    # Test with non-Fibonacci numbers
    assert is_fibonacci(14) == False
    # Test with large numbers that exceed numerical precision
    with pytest.raises(OverflowError):
        is_fibonacci(1e100)
    # Test with non-numeric values
    with pytest.raises(TypeError):
        is_fibonacci("a")


def test_n_Binet():
    # Test with numbers that have a corresponding Fibonacci number
    assert n_Binet(13) == 7
    # Test with numbers that do not have a corresponding Fibonacci number
    assert n_Binet(14) == 7
    # Test with non-numeric values
    with pytest.raises(TypeError):
        n_Binet("a")


def test_nearest_Binet_fib():
    # Test with numbers that have a corresponding Fibonacci number
    assert nearest_Binet_fib(13) == 13
    # Test with numbers that do not have a corresponding Fibonacci number
    assert nearest_Binet_fib(14) == 13
    # Test with non-numeric values
    with pytest.raises(TypeError):
        nearest_Binet_fib("a")


def test_make_saved_Fibonacci_file():
    # Test that the file is created successfully
    make_saved_Fibonacci_file()
    assert True


def test_get_nth_saved_Fibonacci_number():
    # Test with valid indices
    assert get_nth_saved_Fibonacci_number(10) == 34
    # Test with invalid indices
    with pytest.raises(IndexError):
        get_nth_saved_Fibonacci_number(100)
    # Test with non-numeric values
    with pytest.raises(TypeError):
        get_nth_saved_Fibonacci_number("a")
