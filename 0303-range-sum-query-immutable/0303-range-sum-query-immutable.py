class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
    def sumRange(self,left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum_1 = 0
        while(left<=right):
            sum_1 = sum_1+self.nums[left]
            left = left+1
        return sum_1