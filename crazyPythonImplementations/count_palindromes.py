import itertools
from math import comb
class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def check_palindrome(self, st):
        return st == st[::-1]

    def Sub_Sequences(self, STR):
        combs = []
        comb2 = []
        for l in range(1, len(STR)+1):
            combs.append(list(itertools.combinations(STR, l)))
        for c in combs:
            for t in c:
                comb2.append(''.join(t))
        return comb2

    def countPS(self,string):
        # Code here
        combs = self.Sub_Sequences(string)
        res = 0
        palins = []
        for c in combs:
            if self.check_palindrome(c):
                palins.append(c)
                res += 1
        return res
        # print(list(map(self.check_palindrome, combs)))
        # valid = list(map(self.check_palindrome, combs))
        # return sum(list(map(lambda x: 1 if x else 0, valid)))

        
s = Solution()
print(s.countPS('aacb'))


#{ 
 # Driver Code Starts
#Initial template for Python 3
'''
import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends
'''
