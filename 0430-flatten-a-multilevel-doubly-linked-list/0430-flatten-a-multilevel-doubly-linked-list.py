class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        curr = head
        while curr:
            if curr.child:
                nextnode = curr.next
                child = curr.child
                curr.next = child
                child.prev =curr
                curr.child = None
                tail = child
                while tail.next:
                    tail = tail.next
                tail.next = nextnode
                if nextnode:
                    nextnode.prev=tail
            curr = curr.next
        return head