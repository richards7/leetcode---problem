# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if this is a leaf
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            # Backtrack
            path.pop()

        dfs(root, targetSum)

        return result
        