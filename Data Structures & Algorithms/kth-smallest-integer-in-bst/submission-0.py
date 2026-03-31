# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversalHelper(self, root: Optional[TreeNode], res) -> List[int]:  
        if not root:
            return res

        self.inorderTraversalHelper(root.left, res)
        res.append(root.val)
        self.inorderTraversalHelper(root.right, res)

        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        return self.inorderTraversalHelper(root, [])[k-1]