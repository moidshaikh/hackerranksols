class Solution:
    def minJumps(self, arr, n):
        # code here
        last = arr[-1]
        i = 0
        steps = 0
        while i < n:
            if arr[i] == arr[-1]:
                return steps
            i = arr[i]
            steps += 1
        return -1
