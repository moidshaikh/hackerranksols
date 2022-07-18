class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapST, mapTS = {}, {}
        # for c1, c2 in zip(s,t):
        #     if ((c1 in mapST and mapST[c1] != c2) and 
        #         (c2 in mapTS and mapTS[c2] != c1)):
        #         return False
        #     mapST[c1] = c2
        #     mapST[c2] = c1
        # return True
        if s == None or t == None:
            return False
        elif s == "" and t == "":
            return True
        else:
            if len(s) != len(t):
                return False

            lookup = {}   
            for i in range(0, len(s)):
                c1 = s[i]
                c2 = t[i]

                if c1 in lookup:
                    if lookup[c1] != c2:
                        return False
                else:
                    if c2 in lookup.values():
                        return False
                    lookup[c1] = c2

            return True
s = Solution()

print(s.isIsomorphic('badc','baba'))
# print(s.isIsomorphic('add','egg'))