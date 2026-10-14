class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l, r = headA, headB
        while l is not r:
            l =l.next if l else headB
            r = r.next if r else headA
        return l 
        