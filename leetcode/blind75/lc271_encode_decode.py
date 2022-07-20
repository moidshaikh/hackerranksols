class Solution:
    """
    @param:     strs:   a list of strings
    @return:    encodes the list of strings into a single string.

    """

    def encode(self, strs: str) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    """
    @param:     strr:   A string
    @return:    decodes the string into original string.
    
    """

    def decode(self, strr: str) -> str:
        res, i = [], 0
        while i < len(strr):
            j = i
            while strr[j] != "#":
                j += 1
            strlen = int(strr[i:j])
            res.append(strr[j + 1 : j + 1 + strlen])
            i = j + 1 + strlen
        return res


s = Solution()
print(s.decode(s.encode(["ab", "cd"])))
print(s.decode(s.encode(["abcdef", "cdef", "lkjsdf"])))
