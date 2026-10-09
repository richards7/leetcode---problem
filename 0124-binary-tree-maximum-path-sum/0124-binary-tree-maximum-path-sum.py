class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sums = float('-inf')
        def gain(node):
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            price = node.val + left + right
            self.sums = max(self.sums, price)
            return node.val + max(left, right)
        gain(root)
        return self.sums