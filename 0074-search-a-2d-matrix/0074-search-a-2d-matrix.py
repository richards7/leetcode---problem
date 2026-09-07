class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = (l+r)//2
            v = matrix[mid//n][mid%n]
            if v == target:
                return True
            elif v <target:
                l= mid+1
            else:
                r = mid-1
        return False