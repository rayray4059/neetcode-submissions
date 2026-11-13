# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        
        def dfs (node, count):

            if not node:
                return [node, count]
            
            if count == len(out):
                out.append(node.val)

            right = dfs(node.right, count + 1)
            left = dfs(node.left, count + 1)

            return 
        
        dfs(root, 0)
        return out


