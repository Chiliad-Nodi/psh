import pytest

from psh import echo, example
from utils import TestFormatter


@pytest.fixture
def test_formatter():
    return TestFormatter()


def test_example_cmd_should_return_two_things(test_formatter):
    example.chain(test_formatter).call()
    assert "examplecommand" == test_formatter.get_data()


def test_echo_should_echo(test_formatter):
    example.chain(echo).chain(test_formatter).call()
    assert "examplecommand" == test_formatter.get_data()
