from typing import List
class Solution:

    def get_digits(self, no: int) -> int:
        digits = 0
        while no != 0:
            digits += 1
            no = no//10
        if digits % 2 == 0:
            return True
        return False

    def findNumbers(self, nums: List[int]) -> int:
        ...
        # sol1: typecasting and converting to string
        # res = 0
        # for n in nums:
        #     if len(str(n)) % 2 == 0:
        #         res += 1
        # return res

        # Using separate function to calculate no. of digits.

        # evens = [x for x in nums if not self.get_digits(x)]
        # return sum(list(map(self.get_digits, nums)))
        return sum(list(map(self.get_digits, nums)))









s = Solution()
# print(s.get_digits(312))
# print(s.get_digits(1))
# print(s.get_digits(3214))
# print(s.get_digits(87654321345678))

print(s.findNumbers([12,345,2,6,7896]))