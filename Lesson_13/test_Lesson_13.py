# Requests and Pytest
import pytest


@pytest.mark.parametrize("first_num,second_num,expected_sum", [(1, 3, 4), (5, 5, 10)])
def test_check_sum(first_num, second_num, expected_sum):
    assert custom_sum(first_num, second_num) == expected_sum


def custom_sum(first_num, second_num):
    return first_num + second_num
