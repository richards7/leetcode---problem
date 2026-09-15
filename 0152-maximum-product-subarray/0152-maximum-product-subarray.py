class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        mini = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            curr = [nums[i],maxi*nums[i],mini*nums[i]]
            maxi = max(curr)
            mini = min(curr)
            temp = max(temp,maxi)
        return temp
        