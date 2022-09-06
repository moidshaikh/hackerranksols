import pytest

class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1 # base case
        breakpoint()
        
        for i in range(n - 1): # iterating over n 
            temp = one
            one = one + two
            two = temp
        breakpoint()
        return one

s = Solution()
print(s.climbStairs(12))

@pytest.mark.parametrize("n, output", \
            [(0,1), (1,1), 
            (2,2),
            (3,3)])
def test_climb_stairs_null(n, output):
    s = Solution()
    assert s.climbStairs(n) == output