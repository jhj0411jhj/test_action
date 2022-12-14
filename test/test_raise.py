import pytest


def test_raise():
    with pytest.raises(ValueError):
        raise ValueError('a value error')
