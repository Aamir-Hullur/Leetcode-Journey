# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val > val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val)
        return root