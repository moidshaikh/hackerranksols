from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,7,11,15]
        # Two pointers solution. getting it in O(n)
        l, r = 0, len(numbers)-1 # left and right pointers

        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return l+1, r+1

                
            


s = Solution()
numbers = [2,7,11,15]
target = 9
print(s.twoSum(numbers, target))