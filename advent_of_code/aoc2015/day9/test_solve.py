import pytest


from solve import part1
from solve import part2


# @pytest.mark.parametrize(
#     ("i_string", "ret_string"),
#     [
#         ("ugknbfddgicrmopn",True),
#         ("aaa",True),
#         ("jchzalrnumimnmhp",False),
#         ("haegwjzuvuyypxyu",False),
#         ("dvszwmarrgswjxmb",False)
#     ]
# )
# def test_part1(i_string: str, ret_string: bool):
#     assert part1(i_string) == ret_string

@pytest.mark.parametrize(
    ("i_string", "ret_string"),
    [
        (['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141'],605)
    ]
)
def test_part1(i_string: str, ret_string: bool):
    assert part1(i_string) == ret_string