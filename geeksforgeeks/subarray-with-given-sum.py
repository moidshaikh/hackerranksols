class Solution:
    def subArraySum(self, arr, n, s):
        if n < 1:
            return -1
        # initialize sum to first elem in array
        current_sum = arr[0]
        start = 0  # left pointer
        i = 1
        while i <= n:  # iterating over array and adding it to sum.

            while current_sum > s and start < i - 1:
                # if current sum exceeds, remove arr[start] and move left pointer
                current_sum -= arr[start]
                start += 1

            if current_sum == s:  # found the sum
                return start + 1, i

            if i < n:
                current_sum += arr[i]
            i += 1

        return -1


sol = Solution()
# n, s = 74, 665
# arr = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49, 47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124, 138, 139, 119, 83, 130, 142, 34, 116, 40, 59, 105, 131, 178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174, 98, 113]

n, s = 5, 19
arr = [1, 2, 3, 7, 5]

print(sol.subArraySum(arr, n, s))
