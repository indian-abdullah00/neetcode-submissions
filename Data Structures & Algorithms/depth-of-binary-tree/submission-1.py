# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        stack = []
        if root:
            stack.append([root,1])
        while stack:
            num,d = stack.pop()
            if num.left:
                stack.append([num.left,d+1])
            if num.right:
                stack.append([num.right, d+1])
            max_d = max(max_d, d)
            
        return max_d
        