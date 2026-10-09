class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result =[]
        path =[]
        def backtrack(start):
            if len(path)==k:
                result.append(path[:])
                return
            needed = k-len(path)
            remain = n - start+1
            if remain<needed:
                return
            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return result