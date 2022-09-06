#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        if len(A) != len(B):
            return False
        counts = {}
        for i in range(N):
            counts[A[i]] = 1 + counts.get(A[i], 0)
        # print(counts)
        for i in range(N):
            if B[i] not in counts or counts[B[i]] == 0:
                return False
            else:
                counts[B[i]] -= 1 
            # counts[B[i]] = 1 + counts.get(A[i], 0)
        # print(counts)
        return True


        #code here
s = Solution()
n = 10
a = [9, 10, 12, 12, 16, 4, 18, 10, 1, 8]
b = [10, 4, 12, 9, 12, 1, 18, 8, 12, 10]
print(s.check(a,b,n))

# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# if __name__=='__main__':
#     t=int(input())
#     for tc in range(t):
        
#         N=int(input())
        
#         A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
#         B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
#         ob=Solution()
#         if ob.check(A,B,N):
#             print(1)
#         else:
#             print(0)
        
                
                
# # } Driver Code Ends