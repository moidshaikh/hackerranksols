from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # input(f"val at {i}: {nums[i]}")
            # print(f"left sum: {nums[:i]}: {sum(nums[:i])}")
            # print(f"right sum: {nums[i:]}: {sum(nums[i:])}")
            # input()
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

s= Solution()

print(s.pivotIndex([1,7,3,6,5,6]))
