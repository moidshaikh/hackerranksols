#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        return int(str(x)[::-1])


class Solution:
    def reverse(self, x: int) -> int:
        sol, sig = 0, 1
        if x<0:
            sig = -1
            x = x * -1
        while x > 0:
            rem = x % 10
            sol = sol * 10 + rem
            x = x // 10
        if not -2**31<sol<2**31:
            return 0
        return sig * sol


