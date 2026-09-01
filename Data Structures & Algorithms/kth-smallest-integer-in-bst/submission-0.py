# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(root, smallest):
            if not root: return smallest
            helper(root.left, smallest)
            smallest.append(root.val)
            helper(root.right, smallest)
            return smallest
        
        res = []
        return helper(root, res)[k-1]


