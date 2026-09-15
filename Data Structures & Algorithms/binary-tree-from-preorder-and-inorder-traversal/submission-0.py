# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build dict for look up (preorder val: index)
        inord = {v:i for i, v in enumerate(inorder)}
        
        self.pre_index = 0
        def helper(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[self.pre_index])
            self.pre_index += 1
            root_index = inord[root.val]
            root.left = helper(left, root_index - 1)
            root.right = helper(root_index + 1, right)

            return root
        
        return helper(0, len(preorder) - 1)

