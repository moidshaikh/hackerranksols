# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # creating a hashmap of count of each alphabet in the string
        counts = {}
        res = 0
        # using Sliding window, 2 pointer method
        l = 0  # setting up left pointer
        for r in range(len(s)):
            # incrementing the character at s[r] by 1 if not in our hashmap
            counts[s[r]] = 1 + counts.get(s[r], 0)
            # if our sliding window string has duplicate characters, moving the left pointer. and removing it from our count hashmap
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            # updating the result
            res = max(res, r - l + 1)
        # returning result
        return res


s = Solution()

print(s.characterReplacement("AABABBA", 1))
