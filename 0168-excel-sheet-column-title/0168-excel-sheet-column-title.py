class Solution(object):
    def convertToTitle(self, n):
        """
        :type columnNumber: int
        :rtype: str
        """
        result =[]
        while  n >0:
            n = n-1
            r = n %26
            result.append(chr(ord('A')+r))
            n //=26
        return ''.join(reversed(result))