from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = idx = cnt = 0
        while idx < len(nums):
            if nums[idx] == 0:
                idx += 1
            else:
                cnt = 0
                while ((idx<len(nums)) and nums[idx]==1):
                    cnt += 1
                    idx += 1
                res = max(cnt, res)
        return res

s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1,1,1]))