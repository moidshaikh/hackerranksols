class Solution:
    def isAlphaNum(self, c: str) -> bool:
        return (
            (ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) <= ord("z"))  # checking uppercase
            or (ord("0") <= ord(c) <= ord("9"))  # checking lowercase
        )

    def isPalindrome(self, s: str) -> bool:
        # Solution using filter and reverse string function. Memory is more as we're creating s[::-1]
        # s = "".join(filter(str.isalnum, s))
        # l, r = 0, len(s)
        # s = s.lower()
        # return s == s[::-1]

        # Another solution. Using 2 pointers. Time complexity: O(n) memory: O(1)
        l, r = 0, len(s) - 1

        while l < r:
            # check if alphanumeric
            # input(f"{s[l]}, {s[r]}")
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
            # print(f"WHILE END, {l, r}")
        return True


s = Solution()
print(s.isPalindrome("abracadabra"))
print(s.isPalindrome("asdfggfdsa"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
