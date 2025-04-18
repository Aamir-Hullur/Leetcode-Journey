# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # arr = []

        # def dfs(node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)

        # return arr

        arr = []
        stack = []

        while root or stack:
            if not root:
                root = stack.pop()
                arr.append(root.val)
                root = root.right
            else:
                stack.append(root)
                root = root.left
                
        
        return arr

