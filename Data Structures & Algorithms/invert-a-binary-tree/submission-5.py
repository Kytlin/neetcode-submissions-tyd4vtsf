# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            ptr = stack.pop()
            ptr.left, ptr.right = ptr.right, ptr.left
            if ptr.left:
                stack.append(ptr.left)
            if ptr.right:
                stack.append(ptr.right)
        return root