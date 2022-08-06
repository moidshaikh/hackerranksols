# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left: buy, right: sell
        maxp = 0

        while r < len(prices):
            # check if profitable:
            if prices[l] < prices[r]:
                pft = prices[r] - prices[l]
                maxp = max(pft, maxp)
            else:  # not profitable. p[r] is lower than p[l]
                l = r  # shifting left to lowest possible
            r += 1
        return maxp


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
