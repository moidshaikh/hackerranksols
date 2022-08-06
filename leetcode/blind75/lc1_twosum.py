from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            if target - n in visited:
                return visited[target - n], i
            visited[n] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
