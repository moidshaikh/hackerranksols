import pytest


from solve import part1
from solve import part2


@pytest.mark.parametrize(
    ("i_string", "ret_string"),
    [("abcdef",609043),
     ("pqrstuv",1048970)]
)
def test_part1(i_string: str, ret_string: int):
    assert part1(i_string) == ret_string