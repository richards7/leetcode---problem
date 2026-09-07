class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r =0,len(height)-1
        maxwater =0
        while l<r:
            width = r-l
            h = min(height[l],height[r])
            maxwater  = max(maxwater,width*h)
            if (height[l] < height[r]):
                l = l+1
            else:
                r = r-1
        return maxwater