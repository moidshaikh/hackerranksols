from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
      low = 0
      high = len(nums)
      while low<high:
         mid = low + (high-low)//2
         if nums[mid] == target:
            return mid
         if nums[low]<=nums[mid]:
            if target >=nums[low] and target <nums[mid]:
               high = mid
            else:
               low = mid+1
         else:
            if target<=nums[high-1] and target>nums[mid]:
               low = mid+1
            else:
               high = mid
      return -1


s = Solution()
# print(s.search([4,5,6,7,0,1,2],0))
print(s.search([14, 19,0, 1,7,10, 11, 12], -1))
