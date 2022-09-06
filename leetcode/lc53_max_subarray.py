from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        curr_sum = 0
        for i, n in enumerate(nums):
          if curr_sum < 0:
            curr_sum = 0
          curr_sum += n
          maxsub = max(maxsub, curr_sum)
        return maxsub


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
