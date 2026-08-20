class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        curr=0
        mini=float("inf")
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>=target:
                mini=min(mini,right-left+1)
                curr-=nums[left]
                left+=1
        if mini==float('inf'):
            return 0
        return mini