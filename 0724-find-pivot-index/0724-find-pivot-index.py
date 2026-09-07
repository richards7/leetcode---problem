class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_1 = 0
        sum_2 = 0

        for i in range(0,len(nums)):
            sum_1 = sum(nums[:i])
            sum_2 = sum(nums[i+1:])
            if sum_1==sum_2:
                return i
            i = i+1
        return -1