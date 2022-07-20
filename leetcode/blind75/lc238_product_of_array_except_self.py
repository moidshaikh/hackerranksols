from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # gives array of nums except current elem
        # li = {a:[x for x in li if x != a] for a in li}
        # li = [[x for x in nums if x != a] for a in nums]
        # return [math.prod(x) for x in li if x else 0]
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums), -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf([0, 0]))
