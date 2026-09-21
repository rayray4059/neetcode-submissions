# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        out = ""

        def dfs(root):
            nonlocal out
            if not root:
                out = out + "," + "N"
                return None
            
            out += "," + (str(root.val))
            dfs(root.left)
            dfs(root.right)

            return root
        
        dfs(root)
        return out

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data[1:].split(",")
        pointer = 0
        
        def create():
            nonlocal pointer
            if data[pointer] == "N":
                pointer += 1
                return None
            
            node = TreeNode(int(data[pointer]))
            pointer += 1
            node.left = create()
            node.right = create()

            return node

        return create()






