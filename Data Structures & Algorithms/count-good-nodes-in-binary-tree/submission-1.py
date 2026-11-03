# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        def dfs(x, max):
            nonlocal good
            if not x:
                return
            
            if x.val >= max:
                good += 1
                max = x.val
            
            dfs(x.left, max)
            dfs(x.right, max)
        
        dfs(root, -101)
        return good



            

