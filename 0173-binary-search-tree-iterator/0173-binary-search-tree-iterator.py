class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
    def pushLeft(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()

        if node.right is not None:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0