# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        queue = [root]
        while queue:
            lev_width = len(queue)
            lev = []
            for node in range(lev_width):
               current = queue.pop(0)
               if current.left: queue.append(current.left)
               if current.right: queue.append(current.right)
               lev.append(current.val)
            res.append(lev)
        
        return res
            



