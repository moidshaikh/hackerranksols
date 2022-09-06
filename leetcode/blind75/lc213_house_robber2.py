from typing import List
class Solution:
    def house_robber1(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for n in nums:
            prev2, prev1 = max(n+prev1, prev2), prev2
        return prev2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.house_robber1(nums[:-1]), self.house_robber1(nums[1:]))        


s = Solution()
print(s.rob([2,3,2]))
