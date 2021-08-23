# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left<=right:
            mid = (left + right) // 2
            if isBadVersion(mid-1) == False and isBadVersion(mid)== True:
                return mid
            else:
                if isBadVersion(mid) == False:
                    left = mid +1
                else:
                    right = mid -1
        return -1
