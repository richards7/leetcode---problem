class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last = head 
        curr = head.next
        while curr:
            if curr.val>=last.val:
                last = last.next
            else:
                prev = dummy
                while prev.next.val<curr.val:
                    prev = prev.next
                last.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last.next
        return dummy.next
        