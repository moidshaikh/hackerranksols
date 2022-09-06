from curses import nl
from gettext import lngettext
from lib2to3.pgen2.token import NEWLINE
import pytest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = len(res)

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]:
                nlen = r-l+1
                if nlen > reslen:
                    res = s[l:r+1]
                    reslen = nlen
                l -= 1
                r += 1
            # even length:
            i, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                nlen = r-l+1
                if nlen > reslen:
                    res = s[l:r+1]
                    reslen = nlen
                l -= 1
                r += 1
        return res


s = Solution()

@pytest.mark.filterwarnings('ignore::RuntimeWarning')
@pytest.mark.parametrize(
    ("i_string", "ret_string"),
    [("abcdcbe","bcdcb"),
    ("abbbv","bbb"),
    ("abbv","bb"),
    ("abbba","abbba")]
)
def test_longestPalindrome(i_string: str, ret_string: str):
    s = Solution()
    assert s.longestPalindrome(i_string) == ret_string
