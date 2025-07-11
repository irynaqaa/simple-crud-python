import pytest
from noisy_input_API import add_noise, get_data
import numpy as np


def test_add_noise_positive_numbers():
    # Test with a list of positive numbers
    pure_data = [1, 2, 3, 4, 5]
    noisy_data = add_noise(pure_data)
    assert len(noisy_data) == len(pure_data)
    for i in range(len(pure_data)):
        assert np.isclose(noisy_data[i], pure_data[i] * np.random.normal(1, 0.1), atol=0.1)


def test_add_noise_negative_numbers():
    # Test with a list of negative numbers
    pure_data = [-1, -2, -3, -4, -5]
    noisy_data = add_noise(pure_data)
    assert len(noisy_data) == len(pure_data)
    for i in range(len(pure_data)):
        assert np.isclose(noisy_data[i], pure_data[i] * np.random.normal(1, 0.1), atol=0.1)


def test_add_noise_mixed_numbers():
    # Test with a list containing both positive and negative numbers
    pure_data = [1, -2, 3, -4, 5]
    noisy_data = add_noise(pure_data)
    assert len(noisy_data) == len(pure_data)
    for i in range(len(pure_data)):
        assert np.isclose(noisy_data[i], pure_data[i] * np.random.normal(1, 0.1), atol=0.1)


def test_add_noise_empty_list():
    # Test with an empty list
    pure_data = []
    noisy_data = add_noise(pure_data)
    assert len(noisy_data) == len(pure_data)


def test_add_noise_non_numeric_values():
    # Test with a list containing non-numeric values
    pure_data = [1, 'a', 3, 'b', 5]
    with pytest.raises(TypeError):
        add_noise(pure_data)


def test_get_data_valid_input():
    # Test with a valid input value
    num_data_points = 20
    data = get_data(num_data_points)
    assert len(data) == num_data_points


def test_get_data_invalid_input():
    # Test with an invalid input value
    num_data_points = -1
    with pytest.raises(ValueError):
        get_data(num_data_points)


def test_get_data_non_integer_input():
    # Test with a non-integer input value
    num_data_points = 20.5
    with pytest.raises(TypeError):
        get_data(num_data_points)
