import pytest

from solve import part1
from solve import part2


@pytest.mark.parametrize(
    ("i_string", "ret_string"),
    [
        ("ieodomkazucvgmuy",False)
    ]
)
def test_part2(i_string: str, ret_string: bool):
    assert part2(i_string) == ret_string