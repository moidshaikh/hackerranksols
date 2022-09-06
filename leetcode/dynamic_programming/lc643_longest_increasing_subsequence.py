from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                print(LIS)
                # print(i, j, nums[i], nums[j])
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j+1])
        print(LIS)
        return max(LIS)

s = Solution()
# print(s.lengthOfLIS([7,7,7,7,7,7,7]))
# print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))