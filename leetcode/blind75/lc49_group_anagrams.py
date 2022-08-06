from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(list(x))) for x in strs]
        # print(sorted_strs)
        res = {}
        for i, s in enumerate(sorted_strs):
            # print(i,s)
            # input()
            if s in res:
                res[s] += [strs[i]]
            else:
                res[s] = [strs[i]]
        # print(res)
        return list(res.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
