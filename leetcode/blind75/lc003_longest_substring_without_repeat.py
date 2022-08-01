class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Brute Force solution.
        # lss = ''
        # if s == '':
        #     return 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         # print(s[i:j], end='  ')
        #         if len(s[i:j]) > len(lss) and len(s[i:j])==len(set(s[i:j])):
        #             # print("CHANGING LSS")
        #             lss = s[i:j]
        # # print(f"final: {lss}")
        # return len(lss)

        
        # Sliding window. Timecomplexity: O(n)
        subs = set()
        l, res = 0,0
        
        for r in range(len(s)):
            while s[r] in subs:
                subs.remove(s[l])
                l += 1
            subs.add(s[r])
            res = max(res,r-l+1)
        return res



s = Solution()

print(s.lengthOfLongestSubstring('abcabcbb'))
