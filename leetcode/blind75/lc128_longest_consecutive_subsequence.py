from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in nset:
                length = 0
                while (n + length) in nset:
                    length += 1
                longest = max(length, longest)

        return longest


s = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))
