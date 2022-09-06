from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # # return max(sum(nums[::2]), sum(nums[1::2]))
        # dp = [0] * len(nums)
        
        # # base case:
        # if len(nums) == 0:
        #     return 0

        # if len(nums) == 1:
        #     return nums[0]

        # if len(nums) == 2:
        #     return max(nums)

        # # initialize DP array, for base conditions.
        # dp[0] = nums[0]
        # dp[1] = max(nums[:2])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        # # print(dp)
        # return max(dp[-1], dp[-2])
        prev1, prev2 = 0, 0
        for n in nums:
            prev2, prev1 = max(n+prev1, prev2), prev2
        return prev2

s = Solution()
print(s.rob([2,1,1,2]))