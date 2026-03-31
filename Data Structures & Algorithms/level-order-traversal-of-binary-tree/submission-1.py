# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, level = [], []
        depth = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            cur = queue.popleft()
            if depth < cur[1]:
                res.append(level)
                level = []
                depth += 1
            level.append(cur[0].val)

            if cur[0].left:
                queue.append((cur[0].left, depth + 1))
            if cur[0].right:
                queue.append((cur[0].right, depth + 1))
                
        res.append(level)
        return res