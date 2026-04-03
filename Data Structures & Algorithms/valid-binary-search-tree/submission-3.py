# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def traverse(node, left_bound, right_bound):
        #     if not node:
        #         return True
        #     if node.val <= left_bound or node.val >= right_bound:
        #         return False

        #     return traverse(node.left, left_bound, node.val) and traverse(node.right, node.val, right_bound)

        # return traverse(root, -1001, 1001)

        stack = [(root, -1001, 1001)]
        while stack:
            node, left_bound, right_bound = stack.pop()
            if node.val <= left_bound or node.val >= right_bound:
                return False

            if node.left:
                stack.append((node.left, left_bound, node.val))
            if node.right:
                stack.append((node.right, node.val, right_bound))

        return True