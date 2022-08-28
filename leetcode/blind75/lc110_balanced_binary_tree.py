from logging import NullHandler
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0] # base case
            
            left, right = dfs(root.left), dfs(root.right) # calling recursively on left and right subtree
            
            balanced = ( left[0]                            # check if left subtree is balanced.
                         and right[0]                       # check if right subtree is balanced
                         and abs(left[1]-right[1]) <= 1     # check diff of heights of left and right subtree
                        )
            
            return [balanced, 1 + max(left[1], right[1])] # returning balanced and height of subtree
        
        return dfs(root)[0] # returning if tree balanced



s = Solution()
arr = [3,9,20,None,3,15,2,3,3,3,7]
arr = TreeNode(arr)
print(s.isBalanced(arr))
