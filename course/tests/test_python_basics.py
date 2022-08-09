from python_basics import main
from python_basics import __version__

def test_version():
    assert __version__ == '0.1.0'


def test_pass_parameters():
    assert main.passing_arguments(1, 2) == 3
    assert main.passing_arguments(1, -3) == -2