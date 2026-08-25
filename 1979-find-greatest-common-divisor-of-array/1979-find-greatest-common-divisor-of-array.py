class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        small = min(nums)
        largest = max(nums)

        while small!=0:
            largest,small = small,largest%small
        return largest