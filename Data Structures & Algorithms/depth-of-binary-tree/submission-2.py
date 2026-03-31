# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        if not root:
            return 0

        stack = [(root, 0)]
        res = 0
        while stack:
            ptr = stack.pop()
            res = max(res, ptr[1] + 1)
            if ptr[0].left:
                stack.append((ptr[0].left, ptr[1] + 1))
            if ptr[0].right:
                stack.append((ptr[0].right, ptr[1] + 1))
        return res
            