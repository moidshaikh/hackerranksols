# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: # if array has 1 elem. 
            return nums[0]
        # assigning left and right pointers. 
        left, right = 0, len(nums) - 1

        # binary search 
        while left <= right:
            if right - left == 1: # only 2 elements, returning min
                return min(nums[right], nums[left])
                
            if nums[left] < nums[right]: # array is sorted. returning leftmost
                return nums[left]
                
            mid = (left + right) // 2 # midpoint
            if nums[mid] >= nums[left]: # if mid elem is greater, search left sub-array
                left = mid
            else:
                right = mid
        return

s = Solution()

print(s.findMin([3, 4, 5, 1, 2]) == 1)
print(s.findMin([2,3,1]) == 1)

