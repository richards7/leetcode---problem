from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return[]
        result=[]
        queue = deque([root])
        while queue:
            level = len(queue)
            current=[]
            for i in range(level):
                node = queue.popleft()
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current)
        return result