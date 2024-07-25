import pytest


from solve import part1
from solve import part2
from solve import parse_content


@pytest.mark.parametrize(
    ("i_string", "ret_string"),
    [(parse_content(["turn on 0,0 through 999,999"]),1000,000),
     (parse_content(["toggle 0,0 through 999,0"]),1000)]
)
def test_part1(i_string: str, ret_string: int):
    print(i_string)
    assert part1(i_string) == ret_string