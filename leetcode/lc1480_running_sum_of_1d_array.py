def accumsum(lis):
    total = 0
    for x in lis:
        total += x
        yield total

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumsum(nums)
