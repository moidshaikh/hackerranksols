from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        # n = len(nums)
        for i,n in enumerate(nums):
            small_count = 0
            # print(n, nums[i+1:])
            # smaller = [1 for x in nums[i+1:] if x<n]
            small_count += sum([1 for x in nums[i+1:] if x<n])
            # print(f"{small_count=}")
            res.append(small_count)
        return res

s = Solution()
print(s.countSmaller([5,2,6,1]))
