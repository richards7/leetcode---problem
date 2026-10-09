import heapq
class MedianFinder(object):

    def __init__(self):
        self.left = []     
        self.right = []  

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.left, -num)
        value = -heapq.heappop(self.left)
        heapq.heappush(self.right, value)
        if len(self.right) > len(self.left):
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0