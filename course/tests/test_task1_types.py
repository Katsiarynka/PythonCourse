import pytest
from home_tasks.task1_types import get_hello_world,\
get_hello_world_10_times, get_sum, get_sqrt,\
get_factorial, strings_are_equal


def test_get_hello_world():
    assert get_hello_world() == 'Hello World'


def get_hello_world_10_times():
    assert get_hello_world_10_times() == '\n'.join(['Hello World'] * 10)


@pytest.mark.parametrize("arg1,arg2,expected", [(1,2, 3), (2,-4.7, -2.7), (None, 9, 9)])
def test_get_sum(arg1, arg2, expected):
    assert get_sum(1, 2) == 3


def test_get_sqrt():
    assert get_sqrt(4) == 2


def test_get_factorial():
    assert get_factorial(5) == 120


def test_strings_are_equal():
    assert strings_are_equal("Hello", "Hello") == True
    assert strings_are_equal("hello", "Hello") == True
    assert strings_are_equal("hello", "HELLO") == True
    assert strings_are_equal("hello here", "Hello") == False
