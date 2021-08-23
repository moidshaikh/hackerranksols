# # https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_for = {}
        for n,x in enumerate(nums,1):
            try:
                return look_for[x]-1, n-1
            except KeyError:
                look_for.setdefault(target - x,n)
