class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j,n=0,len(t)
        for i in s:
            while j<n and t[j]!=i:
                j+=1
            if j>=n:
                return False
            j+=1
        return True
            
        