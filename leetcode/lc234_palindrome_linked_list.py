from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # mem: O(n), time: first while: O(n) + second while: O(n/2) => O(n)
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l] != nums[r]:
                return False
            l += 1 
            r -= 1
        return True
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # mem: O(n), time: first while: O(1)

        fast = head
        slow = head
        while fast and fast.next: # finding middle of list
            fast = fast.next
            fast = fast.next
            slow = slow.next
        # Slow after first while points at last node
        # reverse the second half. 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # Prev now points to last node
        # Checking for palindrome. 
        left, right = head, prev # right is pointing at last node
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

s = Solution()
li = [1,2,2,1]
print(s.isPalindrome(li))
