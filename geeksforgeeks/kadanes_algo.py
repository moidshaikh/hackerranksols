class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far, curr_max = arr[0], arr[0]
        
        for i in range(1, N):
            input(f"{arr[:i+1]=}")
            curr_max = max(arr[i], arr[i]+curr_max)
            max_so_far = max(curr_max, max_so_far)
            print(f"{curr_max=} {max_so_far=}")
        return max_so_far


s = Solution()
print(s.maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3],len([-2, -3, 4, -1, -2, 1, 5, -3])))