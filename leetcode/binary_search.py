# binary search : https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, el in enumerate(nums):
            if el == target:
                return i
        return -1
