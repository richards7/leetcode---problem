class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        while low<=high:
            d = (low+high)//2
            t=0
            for num in nums:
                t = t+(num+d-1)//d
            if t <=threshold:
                high = d-1
            else:
                low = d+1
        return low