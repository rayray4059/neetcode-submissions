# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(low, high, root):
            if not root: return True
            if low >= root.val or high <= root.val: return False
            return helper(low, root.val, root.left) and helper(root.val, high, root.right)

        return helper(-1000000000, 1000000000, root)