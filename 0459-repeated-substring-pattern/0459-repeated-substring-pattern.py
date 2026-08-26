class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1,n):
            sub = s[:i]
            
            if n % i == 0:
                if sub * (n//i) == s:
                    return True
        
        return False
             
        