# User function template for Python


class Solution:
    def binarysearch(self, arr, n, k):
        # code here
        low, mid, high = 0, 0, n-1
        while low <= high:
            # recalc mid
            print(f"{low=} {mid=} {high=} ")
            mid = (low + high) // 2 
            if arr[mid] == k:# compare mid to target value
                return mid
            elif arr[mid] < k:  
                low = mid + 1
            else:
                high = mid - 1
        return -1


s = Solution()

n = 65
arr_string = '2 3 4 5 7 8 9 11 12 14 15 19 20 22 25 26 28 32 33 35 36 37 38 41 43 44 45 46 49 50 51 52 53 55 59 60 61 62 65 66 67 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 88 92 93 94 95 96 98 99'
arr = list(map(int, arr_string.split()))
k = 222

print(s.binarysearch(arr, n, k))