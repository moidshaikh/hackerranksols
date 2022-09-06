class Solution:
    def reverseInGroups(self, arr, N, K):
        # code here
        # res = []
        # # subgroups = [arr[K*i:K*(i+1)] for i in range(len(arr)//K + 1)]
        # for i in range(len(arr)//K+1):
        #   res.append(arr[K*i:K*(i+1)][::-1])
        #   #sublist = arr[K*i:K*(i+1)][::-1]
        #   #res += ' '.join(sublist)
        # res2 = [val for sublist in res for val in sublist]

        # # res2 = " ".join(res2)
        # for i in range(N):
        #     arr[i] = res2[i]
        i = 0
        while i <= N:
            arr[i: i+K] = arr[i: i+K][::-1]
            i += K
        return arr


n, k = 5, 3
arr = [1,2,3,4,5]
s = Solution()
print(s.reverseInGroups(arr, n, k))