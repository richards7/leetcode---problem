class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        copyhead = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
        return copyhead