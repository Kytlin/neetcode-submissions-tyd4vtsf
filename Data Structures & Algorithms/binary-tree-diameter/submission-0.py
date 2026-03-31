# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(root):
            if not root:
                return 0
            ldepth, rdepth = dfs(root.left), dfs(root.right)

            nonlocal ans
            ans = max(ans, ldepth + rdepth)

            return 1 + max(ldepth, rdepth)

        dfs(root)
        return ans

        