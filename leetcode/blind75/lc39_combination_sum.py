from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # global result

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total > target:
                return
            # two branches of decision
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)

        return res





s = Solution()
print(s.combinationSum([2, 3, 6, 7, 9], 11))
