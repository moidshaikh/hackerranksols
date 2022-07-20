from itertools import count
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # for n in nums:
        #     if n in freq.keys():
        #         freq[n] += 1
        #     else:
        #         freq[n] = 1

        # METHOD 1
        # freq = {x: nums.count(x) for x in set(nums)}
        # res = []
        # while k:
        #     maxval = max(freq.values())
        #     maxkey = [k for k, v in freq.items() if v == maxval][0]
        #     res.append(maxkey)
        #     del freq[maxkey]
        #     k -= 1

        # METHOD 2: n log(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 3], 2))
