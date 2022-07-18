from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = '' # creating result
        for i in range(len(strs[0])): # iterating over chars of first string
            for s in strs: # iterating over all words
                if i == len(s) or s[i] != strs[0][i]:
                    return res # returning result outofbounds or not matching
            res += strs[0][i] # appending to the common words
        return res # finally returning result

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
