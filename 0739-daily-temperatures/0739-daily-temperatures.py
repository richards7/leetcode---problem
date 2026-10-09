class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans =[0]*len(temperatures)
        stack =[]
        i=0
        while i<len(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev]=i-prev
            stack.append(i)
            i = i+1
        return ans