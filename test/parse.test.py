import pytest

from parse import parse_qty


@pytest.mark.parametrize('s, expected', [])
def test_parse_qty(s, expected):
    assert parse_qty(s) == expected

