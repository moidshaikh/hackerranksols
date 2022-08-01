# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # brute force solution. O(n*n)      
        # cursum = []
        # for i in range(0, len(nums)-1):
        #     for j in range(i, len(nums)-1):
        #         # print(nums[i:j])
        #         cursum.append(sum(nums[i:j]))
        # return max(cursum)
        
        # Sliding window solution: O(n)
        maxsub = nums[0]
        current_sum = 0
        
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            maxsub = max(maxsub, current_sum)
        
        return maxsub
