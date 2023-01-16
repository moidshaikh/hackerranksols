import pytest


from solve2 import part1
from solve2 import part2


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
        ("qjhvhtzxzqqjkmpb",True),
        ("xxyxx",True),
        ("uurcxstgmygtbstg",False),
        ("ieodomkazucvgmuy",False)
    ]
)
def test_part2(i_string: str, ret_string: bool):
    assert part2(i_string) == ret_string