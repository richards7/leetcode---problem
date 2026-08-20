class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        sum = nums[0]
        for i in range(len(nums)):
            curr = max(nums[i], curr+nums[i])
            sum = max(curr, sum)
        return sum