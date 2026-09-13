# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        temp_root = root
        stack = []
        if root:
            stack.append(root)
        while stack:
            num = stack.pop()
            num.left , num.right = num.right, num.left
            if num.left:
                stack.append(num.left)
            if num.right:
                stack.append(num.right)

        return root


            
        