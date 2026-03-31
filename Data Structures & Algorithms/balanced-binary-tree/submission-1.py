# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (0, True)

            ltree, rtree = dfs(root.left), dfs(root.right)
            is_balanced = True
            if abs(ltree[0] - rtree[0]) > 1:
                is_balanced = False
            
            return (1 + max(ltree[0], rtree[0]), ltree[1] and rtree[1] and is_balanced)

        return dfs(root)[1]