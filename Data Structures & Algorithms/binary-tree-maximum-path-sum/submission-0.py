# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            left = max(left, 0)
            right = dfs(root.right)
            right = max(right, 0)

            new = root.val + left + right
            if res[0] < new: res[0] = new
            
            return max(left, right) + root.val

        return max(dfs(root), res[0])
        

