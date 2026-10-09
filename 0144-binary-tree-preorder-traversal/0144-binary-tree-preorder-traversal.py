class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result =[]
        def preorder (node):
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result