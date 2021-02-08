import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    path: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            # 말단 노드
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.path = max(self.path, left + right)
            return max(left, right)

        
        dfs(root)
        return self.path


        

